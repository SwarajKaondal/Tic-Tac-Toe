from django.shortcuts import redirect, render
import random
import json
from django.http import JsonResponse
from .main import getCompInput
import ast


def home(request):
    context = {}
    return render(request, 'home.html')


def userInput(request):
    board = request.GET.get('board')
    board = ast.literal_eval(board)
    response = getCompInput(board)
    data = {
        "winner": response[0],
        "move": response[1]
    }
    return JsonResponse(data)
