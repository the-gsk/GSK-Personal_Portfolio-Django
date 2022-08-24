from django.shortcuts import render
from django.contrib import messages
from .models import SendMail
from .forms import UserSendMail
from django.core.mail import send_mail
# Create your views here.

msg = '''[<|message|>]

Hi <|NAME|>,

Thanks so much for writting us about [|<topic|>].

I just wanted to let you know that I'm looking into it and will get back to you before the end of week with an answer.

If you need me to get back to you sooner, please let me know!

Best Regards,
Gaurav Shankar Kumar
'''

def contact_us(request):
    if request.method == 'POST':
        mail_form = UserSendMail(request.POST)
        if mail_form.is_valid():
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            _from = 'heavycoder.in@gmail.com'
            useremail = request.POST.get('useremail')
            mail_data = SendMail(subject=subject, message=message, useremail=useremail)
            mail_data.save()
            msgm=msg.replace("<|message|>", message)
            msgu=msgm.replace("<|NAME|>", useremail)
            msgs=msgu.replace("|<topic|>", subject)
            send_mail(
                subject,
                msgs,
                _from,
                [useremail],
                fail_silently=False,
            )
            mail_form = UserSendMail(request.POST)
            return render (request,'contact/contact.html', {'messages':'Mail Send Successfully'})
        
        else:
            mail_form = UserSendMail(request.POST)

            return render (request,'contact/contact.html', {'messages':'Mail Not Send','form':mail_form})
    else:
        mail_form = UserSendMail(request.POST)
        return render (request,'contact/contact.html', {'messages':'Write','form':mail_form})    