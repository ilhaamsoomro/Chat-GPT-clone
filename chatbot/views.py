from django.shortcuts import render
from django.http import JsonResponse
import openai

# Create your views here.

openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 30,
        n=1,
        stop=None,
        temperature=0.7
    )

    answer = response.choices[0].text.strip()
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response' : response})
    return render(request, 'chatbot.html')