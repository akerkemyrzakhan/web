from django.shortcuts import render

from django.http.request import HttpRequest
from django.http.response import HttpResponse,JsonResponse
# import json

products=[]
for i in range(1,5):
    products.append(
        {
            'id':i,
            'name': f'products{i}',
            'price': i*1000
        }
    )
def product_list(request):
    # data={
    #     'name':'product 1',
    #     'price': 1000
    # }
    # data_str= json.dumps(data)
    # return HttpResponse(data_str, content_type='application/json')
    return HttpResponse(products,safe=False)

def product_detail(request,product_id):
    for product in products:
        if product['id']==product_id:
            return JsonResponse({'error':'product does not exists'})
    # return HttpResponse(f'<h1>product id:{product_id}</h1>')