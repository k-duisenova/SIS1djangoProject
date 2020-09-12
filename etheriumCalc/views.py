# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# shows home page
def home(request):
    return render(request, 'home.html')


# calculates ethereums value in dollars
def calculate(request):
    # input of user - amount of Ethereum
    val1 = int(request.GET['eths'])
    # input of user - checked checkbox type
    if request.GET['eth'] == 'ethe':
        val2 = 367.06
    elif request.GET['eth'] == 'ethec':
        val2 = 5.24
    # calculation of result by multiplying
    res = val1 * val2
    # shows new page where result can be seen
    return render(request, "result.html", {'result': res})

