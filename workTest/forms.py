from django import forms
from django.contrib.auth.forms import UserCreationForm

from workTest.models import Ad, ExchangeProposal


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ["title", "description", "category", "condition"]
        widgets = {
            "condition": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }


class ExchangeProposalForm(forms.ModelForm):
    class Meta:
        model = ExchangeProposal
        fields = ["offered_item", "comments"]
        widgets = {
            "status": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        self.desired_item = kwargs.pop("desired_item", None)
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields["offered_item"].queryset = Ad.objects.filter(
                user=self.user, is_active=True
            )


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
