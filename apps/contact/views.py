from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            content = request.POST.get('content', '')
            # Send email
            email = EmailMessage(
                "LBMCF: New message",
                "From {} <{}>\n\nMessage:\n\n{}\n\nPhone: {}".format(name, email, content, phone),
                "no-reply@lbmcf.br",
                ["glen.jasper7@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                # Ok
                return redirect(reverse('contact_app:url_contact') + '?ok')
            except:
                # Error/Fail
                return redirect(reverse('contact_app:url_contact') + '?fail')

    return render(request,
                  "contact/contact.html",
                  {"context_form": contact_form})
