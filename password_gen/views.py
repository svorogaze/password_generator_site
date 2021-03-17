from django.shortcuts import render
from .modules import password_generator


def home(request):
    if request.method == 'POST':

        lowercase_letters = request.POST.get('lowercase letters') == 'on'
        uppercase_letters = request.POST.get('uppercase letters') == 'on'
        numbers = request.POST.get('numbers') == 'on'
        special_chars = request.POST.get('special chars') == 'on'

        if not request.POST.get('length of password').isdigit():
            return render(request, 'error.html')

        len_of_pass = int(request.POST.get('length of password'))
        if 0 < len_of_pass < 17 and any([lowercase_letters, uppercase_letters, numbers, special_chars]):
            password = password_generator.generate_password(lowercase_letters, uppercase_letters, numbers,
                                                            special_chars,
                                                            len_of_pass)
            return render(request, 'ready_password.html', {'password': password})
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'home.html')
