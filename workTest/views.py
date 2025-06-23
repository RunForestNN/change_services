from urllib.parse import urlparse

import redis

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect, get_object_or_404
from psycopg2 import IntegrityError

from testJob.celery import app
from testJob.settings import CELERY_BROKER_URL
from workTest.tasks import send_exchange_notification
from workTest.forms import AdForm, ExchangeProposalForm, UserCreationFormWithEmail
from workTest.models import Ad, ExchangeProposal


def index(request):
    all_ads = Ad.objects.filter(is_active=True)

    return render(request, "index.html", {"all_ads": all_ads})


def ad_card(request, pk):
    ad = Ad.objects.get(pk=pk)

    return render(request, "ad_card.html", {"ad": ad})


def person_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("person_page")
        else:
            return render(
                request,
                "person_page.html",
                {"error": "Неверное имя пользователя или пароль"},
            )

    if request.user.is_authenticated:
        user_ads = Ad.objects.filter(user=request.user)
        latest_offers = ExchangeProposal.objects.filter(ad_receiver__user=request.user)

        return render(
            request,
            "person_page.html",
            {
                "user": request.user,
                "user_ads": user_ads,
                "latest_offers": latest_offers,
            },
        )
    return render(request, "person_page.html")


def register(request):
    if request.method == "POST":
        form = UserCreationFormWithEmail(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"].lower()
            user.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def edit_ad(request, pk):
    ad = Ad.objects.get(pk=pk)
    if request.method == "POST":
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect("ad_card", pk=ad.id)
    else:
        form = AdForm(instance=ad)

    context = {"form": form, "ad": ad}
    return render(request, "edit_ad.html", context)


@login_required
def delete_ad(request, pk):
    ad = Ad.objects.get(pk=pk)
    ad.delete()
    return redirect("person_page")


@login_required
def create_ad(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            try:
                ad = form.save(commit=False)
                ad.user = request.user
                ad.save()
                messages.success(request, "Объявление успешно создано!")
                return redirect("person_page")
            except IntegrityError as e:
                print(f"Ошибка сохранения: {e}")
    else:
        form = AdForm()
    return render(request, "create_ad.html", {"form": form})


@login_required
def create_offer(request, ad_id):
    desired_item = get_object_or_404(Ad, pk=ad_id, is_active=True)

    if request.method == "POST":
        form = ExchangeProposalForm(
            request.POST, user=request.user, desired_item=desired_item
        )

        if form.is_valid():
            user_ad = Ad.objects.filter(user=request.user, is_active=True).first()
            offer = form.save(commit=False)
            offer.ad_sender = user_ad
            offer.ad_receiver = desired_item
            offer.desired_item = desired_item
            offer.save()
            messages.success(request, "Предложение обмена отправлено")
            print(f"Создано предложение ID: {offer.id}")
            reciv = desired_item.user
            eml = reciv.email
            ttl = desired_item.title
            print(eml)
            print(ttl)
            print(urlparse(CELERY_BROKER_URL).hostname)
            r = redis.Redis(host="localhost", port=6379)
            print(r.ping())  # Должно быть True
            send_exchange_notification.delay(eml, ttl)
            print(app.tasks)
            return redirect("ad_card", pk=desired_item.id)
    else:
        form = ExchangeProposalForm(user=request.user, desired_item=desired_item)
    context = {"form": form, "desired_item": desired_item}

    return render(request, "create_offer.html", context)


@login_required
def manage_offer(request, offer_id, action):
    offer = get_object_or_404(
        ExchangeProposal, pk=offer_id, desired_item__user=request.user
    )

    if action == "accept":
        offer.status = "accepted"
        offer.desired_item.is_active = False
        offer.offered_item.is_active = False
        offer.desired_item.save()
        offer.offered_item.save()

        messages.success(request, "Предложение принято")
    elif action == "reject":
        offer.status = "rejected"
        messages.info(request, "Предложение отклонено")

    offer.save()
    return redirect("person_page")
