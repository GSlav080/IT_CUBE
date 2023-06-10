from django.urls import path
from .views import *

# Отслеживаем переходы
urlpatterns = [
    path('', index, name='home'),
    path('my', MyTask, name='my'),

    path('register', RegisterFormView.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', LogoutUser, name='logout'),
    path('anketa1', ank1, name='anket1'),
    path('anketa2', ank2, name='anket2'),
    path('anketa3', ank3, name='anket3'),
    path('anketa4', ank4, name='anket4'),
    path('anketa5', ank5, name='anket5'),
    path('anketa6', ank6, name='anket6'),
    path('anketa7', ank7, name='anket7'),
    path('update/<int:pk>', Update, name='update'),
    path('del/<int:pk>', DELIT, name='del')

]
