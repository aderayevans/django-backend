from urllib import response
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import mShark
from django.http import JsonResponse

def index(request):
    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles' : ['Admin','User']
    }

    return JsonResponse(responseData)
    # return HttpResponse("return this string")

# Create your views here.
# class IndexView(generic.ListView):
#     # template_name = 'shark/index.html'
#     model = mShark

#     def get_queryset(self):
#         return mShark.getIntro(self)
#         # return HttpResponse("return this string")
