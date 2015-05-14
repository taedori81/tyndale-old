from django import forms
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for

from parsley.decorators import parsleyfy


@parsleyfy
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Your Name'}), max_length=100)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Your Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Subject'}), max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                            'placeholder': 'Your Messages'}))



@processor_for('contact')
def send_emails_from_contact_form(request, page):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject'] + " from " + name
            message = form.cleaned_data['message']

            recipients = ['taedori@outlook.com']

            mail = EmailMessage(subject, message, from_email, recipients)
            mail.send()

            # redirect = request.path + "?sent=1"
            # return HttpResponseRedirect(redirect)

            form = ContactForm()

    return {"form": form}
