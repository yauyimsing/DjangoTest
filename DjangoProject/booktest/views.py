#coding=utf-8
from django.shortcuts import render
from models import *
# Create your views here.
def index(request):
    list = BookInfo.books1.all()
    print('hello kugou')
    for l in list:
        print(l.btitle)
        print('hh......')
    context={'list':list}
    return render(request, 'booktest/index.html', context)
