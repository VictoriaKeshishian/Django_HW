from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging


logger = logging.getLogger(__name__)


def coin(request):
    side = choice(['Орел', 'Решка'])
    logger.debug(side)
    return HttpResponse(side)


def dice(request):
    rnd = randint(1,6)
    logger.debug(rnd)
    return HttpResponse(rnd)


def number(request):
    hundred = randint(1,100)
    logger.debug(hundred)
    return HttpResponse(hundred)
