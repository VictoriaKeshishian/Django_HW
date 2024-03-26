from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging
from .models import CoinFlip

logger = logging.getLogger(__name__)


def coin(request, amount_flips):
    result = choice(('Head', 'Tails'))
    logger.info(result)
    CoinFlip(side=result).save()
    last_results = CoinFlip.get_last_flips(amount_flips)
    context = {
        'current_flip': result,
        'last_results': last_results
    }
    return render(request, 'dice/coin.html', context)


def dice(request):
    rnd = randint(1, 6)
    logger.debug(rnd)
    return HttpResponse(rnd)


def number(request):
    hundred = randint(1, 100)
    logger.debug(hundred)
    return HttpResponse(hundred)
