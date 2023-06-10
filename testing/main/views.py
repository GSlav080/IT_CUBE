
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.contrib.auth.forms import  AuthenticationForm
from .forms import *
from .models import *


# Главная страницв
def index(request):
    info = INFORMATION.objects.all()
    return render(request, 'main/index.html', {'title':'Главная страница', 'info':info})

def ank1(request):
    er = ''
    if request.method == 'POST':
        form = USERFORM(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('home')
        else:
            er = 'ФОРМА БЫЛА НЕВЕРНОЙ'
    form = USERFORM({
        'KURS': "Алгоритмика",
        'USER':request.user
    })
    return render(request, 'main/anketa.html', {'title':'Главная страница', 'form':form, 'error':er})
def ank2(request):
    er = ''
    if request.method == 'POST':
        form = USERFORM(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('home')
        else:
            er = 'ФОРМА БЫЛА НЕВЕРНОЙ'
    form = USERFORM({
        'KURS': "Яндекс лицей",
        'USER': request.user
    })
    return render(request, 'main/anketa.html', {'title':'Главная страница', 'form':form, 'error':er})
def ank3(request):
    er = ''
    if request.method == 'POST':
        form = USERFORM(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('home')
        else:
            er = 'ФОРМА БЫЛА НЕВЕРНОЙ'
    form = USERFORM({
        'KURS': "Робототехника 1-4 класс",
        'USER': request.user
    })
    return render(request, 'main/anketa.html', {'title':'Главная страница', 'form':form, 'error':er})
def ank4(request):
    er = ''
    if request.method == 'POST':
        form = USERFORM(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('home')
        else:
            er = 'ФОРМА БЫЛА НЕВЕРНОЙ'
    form = USERFORM({
        'KURS': "Виртуальная реальность VR/AR",
        'USER': request.user
    })
    return render(request, 'main/anketa.html', {'title':'Главная страница', 'form':form, 'error':er})
def ank5(request):
    er = ''
    if request.method == 'POST':
        form = USERFORM(request.POST)
        if  form.is_valid():
            form.save()
            return  redirect('home')
        else:
            er = 'ФОРМА БЫЛА НЕВЕРНОЙ'
    form = USERFORM({
        'KURS': "Медиа STAR",
        'USER': request.user
    })
    return render(request, 'main/anketa.html', {'title':'Главная страница', 'form':form, 'error':er})
def ank6(request):
    er = ''
    if request.method == 'POST':
        form = USERFORM(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('home')
        else:
            er = 'ФОРМА БЫЛА НЕВЕРНОЙ'
    form = USERFORM({
        'KURS': "Мобильная разработка",
        'USER': request.user
    })
    return render(request, 'main/anketa.html', {'title':'Главная страница', 'form':form, 'error':er})
def ank7(request):
    er = ''
    if request.method == 'POST':
        form = USERFORM(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('home')
        else:
            er = 'ФОРМА БЫЛА НЕВЕРНОЙ'
    form = USERFORM({
        'KURS': "Робототехника 5-8 класс",
        'USER': request.user
    })
    return render(request, 'main/anketa.html', {'title':'Главная страница', 'form':form, 'error':er})


#Регистрация
class RegisterFormView(FormView):
    form_class = RegisterUserForms

    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)

# Авторизация
class LoginUser(LoginView):
    form_class = AuthenticationForm

    template_name = 'main/login.html'

    def form_valid(self, form):
        return super(LoginUser, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginUser, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')

# Выход пользователя
def LogoutUser(request):
    logout(request),
    return redirect('login')

# Мои заявки
def MyTask(request):
    if  request.user.is_superuser:
        table = USER_REG.objects.all()
    else:
        table = USER_REG.objects.filter(USER=request.user)
    print(request.user)
    return render(request, 'main/task.html', {'info': table})

def Update(request, pk):
    template = 'main/anketa.html'
    get_article = USER_REG.objects.get(pk=pk)
    if request.method == 'POST':
        form =USERFORM(request.POST, instance=get_article)
        if form.is_valid():
            form.save()
            return redirect('my')
        else:
            error = 'НЕПРАВИЛЬНОЕ ЗАПОЛНЕНИЕ ФОРМЫ'

    context = {
        'get_article': get_article,
        'update': True,
        'form': USERFORM(instance=get_article)
    }

    return render(request, template, context)


def DELIT(request, pk):
    get_article = USER_REG.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('my'))
