from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .models import ContactMessage



# Create your views here.
class ContactCreateView(CreateView):
    model = ContactMessage
    fields = ['name', 'email', 'message']
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact:success')
    
class ContactSuccessView(TemplateView):
    template_name = 'contact/success.html'