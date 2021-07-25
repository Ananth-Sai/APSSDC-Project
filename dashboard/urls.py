from django.urls import path
from . import views
from user import views as user_view


urlpatterns = [
    path('home/',views.home,name='dashhome'),
    path('staff/',views.staff,name='dashstaff'),
    path('staff/detail/<int:pk>/',views.staff_detail,name='dashstaff_detail'),
    path('product/',views.product,name='dashproduct'),
    path('product/delete/<int:pk>/',views.product_delete,name='dashproduct_delete'),
    path('product/update/<int:pk>/',views.product_update,name='dashproduct_update'),
    path('order/',views.order,name='dashorder'),
    path('accepted/<int:m>/',user_view.accepted,name = 'accepted'),
]
