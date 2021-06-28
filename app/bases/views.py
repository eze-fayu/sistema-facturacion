from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = "bases:login"
    raise_exception = False   # no muestra el error, lo desactiva
    redirect_field_name='redirect_to' #redirecciona
    
    def handle_no_permission(self):       # cuando el usuario no tiene permisos, lo redirreciona a otra url
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser():    # si no es usuario anonimo, es decir si esta logueado
            self.login_url='bases:sin_privilegios'      # lo lleva a sin provilegios sino a login
        return HttpResponseRedirect(reverse_lazy(self.login_url))
    


class Home(LoginRequiredMixin,generic.TemplateView):
    template_name =  'bases/home.html'
    login_url = 'bases:login'
    
class HomeSinPrivilegios(generic.TemplateView):
    template_name =  'bases/sin_privilegios.html'
    # login_url = 'bases:login'