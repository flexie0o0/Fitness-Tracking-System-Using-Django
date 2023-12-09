from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import subprocess
from .models import Food, Consume
from django.contrib.auth.decorators import login_required
#GQxsXz1S59qCs/vSME57bQ==5TYLTgCuhaS4ue4T

# @login_required 
def HomePage(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url= 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers = {'X-Api-Key': 'GQxsXz1S59qCs/vSME57bQ==5TYLTgCuhaS4ue4T'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "Oops, there was an error"
            print(e)
        return render(request, 'users/home.html', {'api': api})
    else:
        return render(request, 'users/home.html', {'query': 'Enter a valid queery'})

# @login_required 
def WorkoutPage(request):
    subprocess.run(["streamlit", "run", "authsysproject/streamlit.py"])
    return render(request, 'users/workout.html')


# def ProfilePage(request):
#     foods = Food.objects.all()
#     consumed_food = Consume.objects.filter(user=request.user)

#     if request.method == "POST":
#         food_consumed = request.POST.get('food_consumed')
#         if food_consumed:
#             try:
#                 consume = Food.objects.get(name=food_consumed)
#                 user = request.user
#                 consume_instance = Consume(user=user, food_consumed=consume)
#                 consume_instance.save()
#             except Food.DoesNotExist:
#                 # Handle the case when the selected food does not exist
#                 pass

#     return render(request, 'users/profile.html', {'foods': foods, 'consumed_food': consumed_food})

@login_required
def ProfilePage(request):
    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')
        if food_consumed:
            try:
                consume = Food.objects.get(name=food_consumed)
                user = request.user
                # Associate the log entry with the currently logged-in user
                consume_instance = Consume(user=user, food_consumed=consume)
                consume_instance.save()
            except Food.DoesNotExist:
                # Handle the case when the selected food does not exist
                pass

    return render(request, 'users/profile.html', {'foods': foods, 'consumed_food': consumed_food})

# @login_required 
def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/home/profile')
    return render(request, 'users/delete.html')


def LoginPage(request):
    if request.method == 'POST':
        if 'signup_submit' in request.POST:
            username = request.POST.get('username')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            weight = request.POST.get('weight')
            height = request.POST.get('height')
            activity = request.POST.get('activity-level')   
            fitness = request.POST.get('fitness-goal')

            if User.objects.filter(username=username).exists():
                return HttpResponse("Error: Username already exists")

            my_user = User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('/')

        elif'login_submit' in request.POST:

            username = request.POST.get('username')
            password1 = request.POST.get('password2')
            user = authenticate(request, username = username, password = password1)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Username or Password is incorrect!")
    

    return render(request, 'users/login.html')


