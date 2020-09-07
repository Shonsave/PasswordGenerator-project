from django.shortcuts import render, get_object_or_404
import random
from .models import Guide


# Create your views here.

def home(request):
    return render(request, 'password_generator/homepage.html')


def genpassword(request):
    return render(request, 'password_generator/genpassword.html')


def testsecurity(request):
    return render(request, 'password_generator/testsecurity.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 8))
    genpassword = ''

    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('Special Characters'):
        characters.extend(list('!@#$%^&*()_-+=:;,.<>?/'))

    for n in range(length):
        genpassword += random.choice(characters)

    return render(request, 'password_generator/password.html', {'password': genpassword})


def security(request):
    user_password = request.GET.get('password')

    lowercase = 'qwertyuiopasdfghjklzxcvbnm'
    uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    numbers = '1234567890'
    specials = '!@#$%^&*()_-+=:;,.<>?/ '
    passpecials = 0
    pasuppers = 0
    paslowers = 0
    pasnumbers = 0
    score = 0

    for letter in user_password:
        if letter in lowercase:
            paslowers += 1
            score += 1

        elif letter in uppercase:
            pasuppers += 1
            score += 2

        elif letter in specials:
            passpecials += 1
            score += 3

        elif letter in numbers:
            pasnumbers += 1
            score += 1

    if score < 5:
        security = 'Terrible!'
        col = 'r'

    elif score < 7 and score > 4:
        security = 'Very Low'
        col = 'r'

    elif score < 10 and score > 6:
        security = 'Low'
        col = 'r'

    elif score < 14 and score > 9:
        security = 'Average'
        col = 'y'

    elif score < 19 and score > 13:
        security = 'Secure'
        col = 'g'

    elif score < 25 and score > 18:
        security = 'High'
        col = 'g'

    elif score < 29 and score > 24:
        security = 'Very High'
        col = 'g'

    elif score > 28:
        security = 'Virtually Unhackable!'
        col = 'b'

    return render(request, 'password_generator/security.html',
                  {'lowercase': paslowers, 'uppercase': pasuppers, 'specials': passpecials, 'numbers': pasnumbers,
                   'security_level': security, 'score': score, 'col': col})


def maingiude(request):
    guides = Guide.objects.order_by('-date')
    return render(request, 'password_generator/info.html', {'blogs': guides})


def full_blog(request, blog_id):
    blog = get_object_or_404(Guide, pk=blog_id)
    return render(request, 'password_generator/full_blog.html', {'blog': blog})
