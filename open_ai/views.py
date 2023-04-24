from django.shortcuts import render, redirect
# import openai library
import openai


# Set up the OpenAI API client


# Create your views here.
def chatresponse(request):
    context={}
    data = request.POST
    if data:
        question = data.get("question")
        if question:
            model_engine = "text-davinci-003"

            completion = openai.Completion.create(
                engine=model_engine,
                prompt=question,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )

    # extracting useful part of response
            return_data = completion.choices[0].text
            context['return_data'] = return_data
            print(completion)

    return render (request,'open_api/chat.html',context)


