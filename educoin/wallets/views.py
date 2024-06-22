# wallets/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Wallet
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_wallet(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student_name = data.get('student_name')
        if Wallet.objects.filter(student_name=student_name).exists():
            return JsonResponse({'message': 'Wallet already exists!'}, status=400)
        wallet = Wallet(student_name=student_name)
        wallet.save()
        return JsonResponse({'message': 'Wallet created!', 'student_name': student_name})

@csrf_exempt
def add_coins(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student_name = data.get('student_name')
        amount = data.get('amount')
        try:
            wallet = Wallet.objects.get(student_name=student_name)
            wallet.balance += amount
            wallet.save()
            return JsonResponse({'message': 'Coins added!', 'new_balance': wallet.balance})
        except Wallet.DoesNotExist:
            return JsonResponse({'message': 'Wallet not found!'}, status=404)

def get_balance(request, student_name):
    try:
        wallet = Wallet.objects.get(student_name=student_name)
        return JsonResponse({'balance': wallet.balance})
    except Wallet.DoesNotExist:
        return JsonResponse({'message': 'Wallet not found!'}, status=404)

