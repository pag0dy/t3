from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse('Inicio')


def register(request):
    return HttpResponse('Registrar')
