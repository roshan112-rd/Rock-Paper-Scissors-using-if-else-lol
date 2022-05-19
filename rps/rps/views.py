from django.shortcuts import render
import random
from django.contrib import messages
def home(request):
    comp_value= ['rock', 'paper', 'scissors']
    comp_random = random.choice(comp_value)
    if request.method == 'POST':
        value = request.POST['value']
        if (comp_random=='rock'):
            if(value=='rock'):
                messages.error(request, 'try again.')
            elif(value == 'paper'):
                messages.error(request, 'you won')
            else:
                messages.error(request, 'you lost')
        elif(comp_random == 'paper'):
            if(value=='rock'):
                messages.error(request, 'you lost')
            elif(value == 'paper'):
                messages.error(request, 'try again.')
            else:
                messages.error(request, 'you won')
        elif(comp_random == 'scissors'):
            if(value=='rock'):
                messages.error(request, 'you won')
            elif(value == 'paper'):
                messages.error(request, 'try again.')
            else:
                messages.error(request, 'try again')
        else:
            messages.error(request, 'computer is dead! You won.')
    return render (request, 'home.html',{'comp_random':comp_random, 'value':value})