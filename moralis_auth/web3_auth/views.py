import json
import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from datetime import datetime, timedelta, timezone

API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IjEzZmQyNzY4LTNhNmItNDRkZi1hZTcyLWFmMzUyMzBhYzE5MiIsIm9yZ0lkIjoiODQ0NzUiLCJ1c2VySWQiOiI4NDExOSIsInR5cGVJZCI6IjdjZjQ3ZTQ3LTExNmMtNGRmYS04NzgwLTUxMDM3NWE0NmE1NCIsInR5cGUiOiJQUk9KRUNUIiwiaWF0IjoxNjg3NTYzMTE2LCJleHAiOjQ4NDMzMjMxMTZ9.vCUGn7vwG5_5cPootEMw3oXoX5BO1Knch2fSitAOFmw'
# this is a check to make sure the the API key was set
# you have to set the API key only in line 9 above
# you don't have to change the next line
if API_KEY == 'WEB3_API_KEY_HERE':
    print("API key is not set")
    raise SystemExit


def moralis_auth(request):
    return render(request, 'login.html', {})

def my_profile(request):
    return render(request, 'profile.html', {})

def chainlitUI(request):
    return redirect()

def request_message(request):
    data = json.loads(request.body)
    print(data)


    #setting request expiration time to 1 minute after the present->
    present = datetime.now(timezone.utc)
    present_plus_one_m = present + timedelta(minutes=1)
    expirationTime = str(present_plus_one_m.isoformat())
    expirationTime = str(expirationTime[:-6]) + 'Z'

    REQUEST_URL = 'https://authapi.moralis.io/challenge/request/evm'
    request_object = {
      "domain": "defi.finance",
      "chainId": 1,
      "address": data['address'],
      "statement": "Please confirm",
      "uri": "https://defi.finance/",
      "expirationTime": expirationTime,
      "notBefore": "2020-01-01T00:00:00.000Z",
      "timeout": 15
    }
    x = requests.post(
        REQUEST_URL,
        json=request_object,
        headers={'X-API-KEY': API_KEY})

    return JsonResponse(json.loads(x.text))


def verify_message(request):
    data = json.loads(request.body)
    print(data)

    REQUEST_URL = 'https://authapi.moralis.io/challenge/verify/evm'
    x = requests.post(
        REQUEST_URL,
        json=data,
        headers={'X-API-KEY': API_KEY})
    print(json.loads(x.text))
    print(x.status_code)
    if x.status_code == 201:
        # user can authenticate
        eth_address=json.loads(x.text).get('address')
        print("eth address", eth_address)
        try:
            user = User.objects.get(username=eth_address)
            HttpResponseRedirect('http://localhost:8000')
        except User.DoesNotExist:
            user = User(username=eth_address)
            user.is_staff = False
            user.is_superuser = False
            user.save()
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['auth_info'] = data
                request.session['verified_data'] = json.loads(x.text)
                HttpResponseRedirect('http://localhost:8000')
                return JsonResponse({'user': user.username})
            else:
                return JsonResponse({'error': 'account disabled'})
    else:
        return JsonResponse(json.loads(x.text))