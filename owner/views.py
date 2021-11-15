from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views import View
from owner.models import Owner, Dog

# OwnerView
class OwnerView(View): 
    # post 기능
    def post(self, request): 
        '''
        1. 함수의 목적: 정보를 데이터베이스에 insert gksek.
        2. input : 요청받은 정보
        3. 데이터베이스에 정보 등록
        4. output: 상태코드, pk, 메세지, 요청 받은 정보 등
        '''
        # input은 어디에?: http의 request의 body에 있다.
        data = json.loads(request.body)
        Owner.objects.create(
            name  = data['name'],
            age   = data['age'],
            email = data['email']
        )
        return JsonResponse({"MESSAGE" : "CREATED"}, status = 201)
    # get 기능
    def get(self, request): 
        owners  = Owner.objects.all()
        results = []
        for owner in owners: 
            results.append(
                {
                    'name' : owner.name,
                    'email': owner.email,
                    'age'  : owner.age,
                    'dog'  : [x.name for x in owner.dog_set.all()]
                }
            )
        return JsonResponse({'results' : results}, status = 200)

# DogView
class DogView(View): 
    # post 기능
    def post(self, request): 
        data  = json.loads(request.body)
        owner = Owner.objects.get(name = data['owner'])
        Dog.objects.create(
            owner = owner,
            name  = data['name'],
            age   = data['age'],
        )
        return JsonResponse({"MESSAGE" : "CREATED"}, status = 201)
    # get 기능
    def get(self, request): 
        dogs    = Dog.objects.all()
        results = []
        for dog in dogs: 
            results.append(
                {
                    'owner': dog.owner.name,
                    'name' : dog.name,
                    'age'  : dog.age
                }
            )
        return JsonResponse({'results' : results}, status = 200)