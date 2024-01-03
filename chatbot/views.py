from django.shortcuts import render
from django.http import JsonResponse
import openai

# Create your views here.

openai_api_key = 'Your OpenAi API key' #redacted for privacy
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role" : "system", "content" : "You are a helpful assistant."},
            {"role" : "user", "content" : message},
        ],
        # prompt = message,
        max_tokens = 10,
        # n=1,
        # stop=None,
        # temperature=0.2
    )
    print(response)
    #answer = response.choices[0].text.strip()
    answer = response.choices[0].message.content.strip()
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response' : response})
    return render(request, 'chatbot.html')