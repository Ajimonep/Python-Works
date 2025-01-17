from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render


class HelloWorldView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("Hello World")

class GoodMorningView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("Good morning")

class GoodAfternoonView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("Good Afternoon")

class GoodEveningView(View):
        def get(self,request,*args,**kwargs):
            return HttpResponse("Good Evening")

class GoodNightView(View):
        def get(self,request,*args,**kwargs):
            return HttpResponse("Good Night")

class SelfIntroView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"selfintro.html")


class FrameworkView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"framework.html")



    