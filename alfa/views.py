from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ComprarForm  
from django.contrib.auth.decorators import  login_required

def home(request):
    return render(request, "home.html")

def registro(request):
    form = UserCreationForm()
    if request.method == 'GET':
        return render(request, "registro.html", {"form": form})
    else:
        req = request.POST
        if req['password1'] == req['password2']:
            try:
                user = User.objects.create_user(
                    username=req['username'], 
                    password=req['password1']
                )
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, "registro.html", {
                    "form": form, 
                    "msg": "El usuario ya existe"
                })
            except Exception as e:
                return render(request, "registro.html", {
                    "form": form, 
                    "msg": f"Ocurrió el siguiente error: {e}. Intente de nuevo"
                })
        else:
            return render(request, "registro.html", {
                "form": form,
                "msg": "Las contraseñas no coinciden"
            })

def iniciarsesion(request):
    if request.method == 'GET':
        return render(request, "login.html", {
            "form": AuthenticationForm(),  # Crear una instancia del formulario
        })
    else:
        try:
            user = authenticate(request=request,
                                username=request.POST["username"], password=request.POST["password"])
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return render(request, "login.html", {
                    "form": AuthenticationForm(),
                    "msg": "Usuario o contraseña incorrecta",
                })
        except Exception as e:
            return render(request, "login.html", {
                "form": AuthenticationForm(),
                "msg": f"Ocurrió un error: {e}",
            })

def cerrarsesion(request):
    logout(request)
    return redirect("/")

@login_required
def comprar(request): 
    if request.method == "GET":
        return render(request, "comprar.html", {
            "form": ComprarForm(),  
        })
    else:
        try:
            form=ComprarForm(request.POST)
            if form.is_valid ():
                nuevo=form.save(commit=False)
                if request.user.is_authenticated:
                    nuevo.user=request.user
                    nuevo.save()
                    return redirect("/")
                else:
                    return render(request, "comprar.html", {
                    "form": ComprarForm(),  
                    "msg": "AUTENTICATE TONOTO",
            }) 
            else:
                return render(request, "comprar.html", {
                "form": ComprarForm(),  
                "msg": "Error en el formulario",
            })
        except Exception as e:
            return render(request, "comprar.html", {
                "form": ComprarForm(),  
                "msg": f"Ocurrio un error",
            })