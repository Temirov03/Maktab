from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request,yosh):
    context = {"lugat":{"ism":"Ali","familiya":"Valiyev"},
               "name":"Nurbek",
               "surname":"Temirov",
               "yosh":yosh}
    return render(request,"index.html",context)
