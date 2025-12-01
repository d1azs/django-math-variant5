from django.contrib import admin
from django.urls import path
from mathapp import views as math_views
from guessgame_app import views as guess_views
from hello_app import views as hello_views
from warehouse_app import views as warehouse_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', math_views.index, name='index'),

    path('quadratic/', math_views.quadratic_view, name='quadratic'),
    path('result/', math_views.result_view, name='result'),

    path('feedback/', math_views.feedback_view, name='feedback'),
    path('rating/', math_views.rating_view, name='rating'),

    path('guess/', guess_views.guess_view, name='guess'),
    path('guess/submit/', guess_views.guess_submit, name='guess_submit'),

    path('hello/', hello_views.hello_view, name='hello'),

    path('products/', warehouse_views.ProductListView.as_view(), name='products'),
    path('products/create/', warehouse_views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', warehouse_views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', warehouse_views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', warehouse_views.ProductDeleteView.as_view(), name='product_delete'),

    path('replenish/<int:count>/', warehouse_views.replenish_view, name='replenish'),
    path('replenish/<int:count>/', warehouse_views.replenish_view, name='replenish'),
]