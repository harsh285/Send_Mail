from django.urls import path
from send_mail.views import InformationCreate, send_mail_test, home, TakeEmailCreate, finalpage

urlpatterns = [
    path('', home, name="home"),
    path('InformationCreate', InformationCreate.as_view(), name='information'),
    path('TakeEmailCreate', TakeEmailCreate.as_view(), name='takeEmail'),
    path('finalpage/', finalpage, name='finalpage'),
]
