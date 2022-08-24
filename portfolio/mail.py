from django.core.mail import send_mail


msg = '''[<|message|>]

Hi <|NAME|>,

Thanks so much for writting us.

I just wanted to let you know that I'm looking into it and will get back to you before the end of week with an answer.

If you need me to get back to you sooner, please let me know!

Best Regards,
Gaurav Shankar Kumar
'''

if request.POST:
            user_name = request.POST.get('user_name')
            message = request.POST.get('user_message')
            _from = 'heavycoder.in@gmail.com'
            useremail = request.POST.get('user_email')
            mail_data = SendMail(subject=user_name, message=message, useremail=useremail)
            mail_data.save()
            msgm=msg.replace("<|message|>", message)
            msgu=msgm.replace("<|NAME|>", user_name)
            send_mail(
                'HeavyCoder',
                msgu,
                _from,
                [useremail],
                fail_silently=False,
            )