from django.urls import path
from core.views import product_list,product_detail,category_detail,category_list,products_in_category
urlpatterns=[
    path('products/', product_list),
    path('products/<int:product_id>/',product_detail),
    path('categories/',category_list ),
    path('categories/<int:category_id>',category_detail),
    path('categories/<int:id>/products',products_in_category ),

]