# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def calculate(request):
    val1 = int(request.GET['eths'])
    if request.GET['eth'] == 'ethe':
        val2 = 367.06
    elif request.GET['eth'] == 'ethec':
        val2 = 5.24
    res = val1 * val2

    return render(request, "result.html", {'result': res})

