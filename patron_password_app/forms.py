from django import forms
from django.core import validators
from patron_password_app.models import Patron, GoogleAccount, YahooAccount, HotmailAccount, OtherAccount


class SearchForm(forms.Form):
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    cardnumber = forms.CharField(required=False)


class EditForm(forms.Form):
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    cardnumber = forms.CharField(required=False)
    phonenumber = forms.CharField(required=False)
    gusername = forms.CharField(required=False)
    gpassword = forms.CharField(required=False)
    yusername = forms.CharField(required=False)
    ypassword = forms.CharField(required=False)
    husername = forms.CharField(required=False)
    hpassword = forms.CharField(required=False)
    oservice = forms.CharField(required=False)
    ousername = forms.CharField(required=False)
    opassword = forms.CharField(required=False)

class PatronForm(forms.ModelForm):
    class Meta():
        model = Patron
        fields = ('__all__')

class GoogleForm(forms.ModelForm):
    class Meta():
        model = GoogleAccount
        fields = ('__all__')

class YahooForm(forms.ModelForm):
    class Meta():
        model = YahooAccount
        fields = ('__all__')

class HotmailForm(forms.ModelForm):
    class Meta():
        model = HotmailAccount
        fields = ('__all__')

class OtherForm(forms.ModelForm):
    class Meta():
        model = OtherAccount
        fields = ('__all__')
