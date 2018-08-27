from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlparse, parse_qs

from licence.models import Licence

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index/index.html'
    context_object_name = 'licencesList'

    def get_queryset(self):
        return Licence.objects.order_by('name').all()

class DocumentsView(generic.ListView):
    template_name = 'index/documents.html'

    def get_queryset(self):
        return

def LoginView(request):
    errorMessage = None
    user = None

    if request.GET.get('next') is not None:
        next = '?next=' + request.GET.get('next')
    else:
        next = ''

    if request.POST:
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/' if request.GET.get('next') is None else request.GET.get('next'))
            else:
                errorMessage = 'Combinaison utilisateur/mot de de passe incorrect.'
        else:
            errorMessage = 'Erreur lors de la soumission du formulaire, veuillez réessayer.'

    greetings = {
        'testPost': request.POST,
        'errorMessage': errorMessage,
        'user': user,
        'next': next
    }
    return render(request, 'index/login.html', greetings)

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('index:home'))
