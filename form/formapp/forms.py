from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(
        label = "Enter your first name :" ,
        widget = forms.TextInput(
            attrs = {
                'class' : "form-control" ,
                'placeholder' : "Your name",
            }
        )
    )

    last_name = forms.CharField(
        label = "Enter your last name :" ,
        widget = forms.TextInput(
            attrs = {
                'class' : "form-control" ,
                'placeholder' : "Your last name",
            }
        )
    )
    email = forms.EmailField(
        label = "Enter your Email :" ,
        widget = forms.EmailInput(
            attrs = {
                'class' : "form-control" ,
                'placeholder' : "Your E-mail",
            }
        )
    )
    mobile = forms.IntegerField(
        label = "Enter your mobile :" ,
        widget = forms.NumberInput(
            attrs = {
                'class' : "form-control" ,
                'placeholder' : "Your last name",
            }
        )
    )

    loc = forms.CharField(
        label = "Enter your location :" ,
        widget = forms.TextInput(
            attrs = {
                'class' : "form-control" ,
                'placeholder' : "Your location",
            }
        )
    )