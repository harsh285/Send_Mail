from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from send_mail.forms import UserEmail, InformationCreateForm, TakeEmailCreateForm
from django.shortcuts import render, get_object_or_404
from mail_service.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from send_mail.models import Information, TakeEmail


def home(request):
    return render(request, 'home.html')


class TakeEmailCreate(CreateView):
    model = TakeEmail
    form_class = TakeEmailCreateForm
    template_name = 'take_email.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        return super(TakeEmailCreate, self).post(request, *args, **kwargs)


class InformationCreate(CreateView):
    model = Information
    form_class = InformationCreateForm
    template_name = 'information.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('finalpage')

    def post(self, request, *args, **kwargs):
        return super(InformationCreate, self).post(request, *args, **kwargs)


def finalpage(request):
    if request.method == 'POST':
        data = request.POST
        selected_email = get_object_or_404(TakeEmail, id=request.POST.get('select_email'))
        send_mail_test(selected_email)
        return render(request, 'success.html', {'recepient': selected_email})
    else:
        data = TakeEmail.objects.all()
    return render(request, 'index.html', {'data': data})


def send_mail_test(emailid):
    data: Information = Information.objects.all().order_by('-created_at').first()
    subject = 'Product Information That you Submited at LocalHost'
    message = 'Here Some Information About The Product you Have Recently Added.' + '\n\nProduct Name :' + str(
        data.product_name) + '\nCategory :' + str(data.Category) + '\nQuantity : ' + str(data.Qty) + '\nPrice : ' + str(
        data.price) + '\n\n Your Total Amount :' + str(float(data.Qty) * float(data.price))
    recepient = str(emailid)
    send_mail(subject,
              message, EMAIL_HOST_USER, [recepient], fail_silently=False)
