from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import User, Question
from random import randint
from datetime import datetime

user_name = None
ans = None

def quiz(request):
    global user_name
    global ans

    que_data = Question.objects.all()
    total_que = len(que_data)-1

    num1 = randint(0, total_que)
    num2 = None
    while not num2:
        temp_num2 = randint(0, total_que)
        if temp_num2 != num1:
            num2 = temp_num2
    
    que1 = Question.objects.filter(Question_ID = que_data[num1])
    que2 = Question.objects.filter(Question_ID = que_data[num2])

    if request.method == "POST":
        ans = ""
        ans1 = request.POST.get("ans1")
        ans2 = request.POST.get("ans2")
        if ans1 == que1[0].Answer:
            ans += "True"
        else:
            ans += "False"
        ans += " "
        if ans2 == que2[0].Answer:
            ans += "True"
        else:
            ans += "False"
        
        return redirect("/thanks")

    time_now = str(datetime.strptime(user_name.time_history, r'%Y-%m-%d %H:%M:%S.%f'))


    return render(request, "main/quiz.html", {"que1":que1, "que2":que2, "time_now":time_now, "user_name":user_name})

def home(request):
    global user_name

    message = None

    if request.method == "POST":
        email = request.POST.get("email")
        print(email)
        user = User.objects.filter(Email = email)
        if user:
            user_name = user[0]
            print(user_name)
            if not user[0].time_history:
                user[0].time_history = str(datetime.now())
                user[0].save()

            return redirect("/quiz")
        else:
            message = f"User not found for {email}. Please enter a valid email ID."

    return render(request, "main/index.html", {"message": message})


def thanks(request):
    global user_name
    global ans

    user_name.time_history = None
    user_name.result = ans
    user_name.save()

    return render(request, 'main/thanks.html', {"user_name":user_name})