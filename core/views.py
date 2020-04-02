from django.http.response import JsonResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from core.models import Product,Category
@csrf_exempt
def product_list(request):
    if request.method =='GET':
        products=Product.objects.all()
        products_json = [product.to_json() for product in products]
        return JsonResponse(products_json,safe=False)
    elif request.method == 'POST':
        pass
@csrf_exempt
def product_detail(request,product_id):
    try:
        product=Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        # raise Http404
        return JsonResponse({'error':str(e)})
    if request.method=='GET':
        return JsonResponse(product.to_json())
    elif request.method=='PUT':
        pass
    elif request.method=='DELETE':
        pass

def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def category_detail(request,category_id):
    try:
        category=Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        # raise Http404
        return JsonResponse({'error':str(e)})
    return JsonResponse(category.to_json())

def products_in_category(request,id):
    try:
        product_in_category = Product.objects.filter(category_id=id)
        product_in_category_json = [product.to_json() for product in product_in_category]
    except Category.DoesNotExist as e:
        # raise Http404
        return JsonResponse({'error':str(e)})
    return JsonResponse(product_in_category_json, safe=False)

