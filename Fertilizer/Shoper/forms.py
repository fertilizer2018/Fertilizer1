from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#login form in shoper user name and password

class ShoperForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField()

    def clean(self):
        cleaned_data = super(ShoperForm, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError(
                "That user is already taken , please select another ")

        return cleaned_data
#Regestration forms

class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    mobile_number = forms.CharField(required=True)
    email = forms.EmailField(required = True)
    address = forms.CharField(required = False)
    zipcode = forms.CharField(required = False)
    password1 = forms.CharField(widget=forms.PasswordInput(), label='password')
    password2 = forms.CharField(label='confirme password')
    class Meta:
        model = User
        fields = ('username', 'mobile_number', 'email', 'address', 'zipcode', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(MyRegistrationForm, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError(
                "That user is already taken , please select another ")

        return cleaned_data


class ShoperSignup(MyRegistrationForm):
    Pancard = forms.CharField(required=True)
    GST = forms.CharField(required=True)
    ShopName = forms.CharField(required=True)
    ShopLicense = forms.CharField(required=True)
    ShopDocument=forms.ImageField(required=True)
    class Meta:
        model = User
        fields = ('username', 'mobile_number', 'email', 'address', 'zipcode','Pancard', 'GST', 'ShopName', 'ShopLicense', 'ShopDocument', 'password1', 'password2')

    def save(self,commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
        user.mobile_number = self.cleaned_data['mobile_number']
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']

        if commit:
            user.save()
        return user

