from django.urls import path,re_path
from . import views

# from project.views import product_list, product_detail


urlpatterns = {
    path('products/', views.product_list),
    # re_path(r'products/<[a-z0-9]>', product_list),
    path('products/<int:product_id>',views.product_detail),
}
