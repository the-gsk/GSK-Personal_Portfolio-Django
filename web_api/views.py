from django.shortcuts import render, redirect
from django.http.response import JsonResponse
import difflib
from django.views.decorators.csrf import csrf_exempt
from contact.models import SendMail
from django.core.mail import send_mail
from django.contrib import messages


msg = '''[<|message|>]

Hi <|NAME|>,

Thanks so much for writting us.

I just wanted to let you know that I'm looking into it and will get back to you before the end of week with an answer.

If you need me to get back to you sooner, please let me know!

Best Regards,
Gaurav Shankar Kumar
'''


# import openai library
import openai


# Set up the OpenAI API client


def get_best_match(question, threshold=0.8):
    qa_dict = {
            "What is your name?": "My name is Indu 2.0." ,
            "your name?": "My name is Indu 2.0." ,
            "Who is your father?": "My Father is Gaurav Shankar Kumar.",
            "father name?": "My Father is Gaurav Shankar Kumar.",
            "What can you do?": "I can answer questions, write stories, and much more.",
            "How do you work?":  "I use advanced machine learning algorithms to understand and respond to natural language input.",
        }
    best_match = None
    best_score = 0
    for q in qa_dict.keys():
        score = difflib.SequenceMatcher(None, question, q).ratio()
        if score > best_score and score >= threshold:
            best_match = q
            best_score = score
    return qa_dict.get(best_match, None)


# Create your views here.
def chatresponse(request):
    return render (request,'open_api/chat.html')


def universal_response(request):
    data = request.POST
    question = data.get("question")
    if question:
        model_engine = "text-davinci-003"
        return_data = get_best_match(question)
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
            # extracting useful part of response
        if return_data is None:
            return_data = completion.choices[0].text

        return JsonResponse(data = {'data':return_data})
    return JsonResponse(data = {'data':'If you are Bad I am your DAD!'})

@csrf_exempt
def send_email(request):
    try:
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
                [useremail,'gauravshankarkumar@gmail.com'],
                fail_silently=False,
            )
            return JsonResponse(data = {'data': "Your Email Sent Successfully!"},status=200)
    except Exception as e:
        return JsonResponse(data = {'data': f"{e}"},status=200)

