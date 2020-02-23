from django.shortcuts import render
from .models import ContactData
from .forms import ContactForm
from django.http import HttpResponse


# Create your views here.
def contact_view(request):
    if request.method == 'GET':
        cform = ContactForm 
        return render(request,'contact_form.html',{'abcd': cform })
    else:
        cform = ContactForm(request.POST)
        if cform.is_valid():
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            email1 = request.POST.get('email')
            mobile1 = request.POST.get('mobile')
            loc1 = request.POST.get('loc')

            data = ContactData(
                first_name= fname ,
                last_name= lname,
                email=email1,
                mobile=mobile1,
                loc=loc1,
            )
            data.save()
            cform = ContactForm()
            return render (request,'contact_form.html',{'abcd' : cform })
        else:
            return HttpResponse("missed")


