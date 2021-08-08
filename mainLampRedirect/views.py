from django.shortcuts import render
import requests


def turn_on_desk_lamp(request):
    requests.get("http://2.tcp.ngrok.io:13366/27/on")
    return render(request, "mainLampRedirect/index.html", context={})


def turn_of_desk_lamp(request):
    requests.get("http://2.tcp.ngrok.io:13366/27/off")
    return render(request, "mainLampRedirect/index.html", context={})