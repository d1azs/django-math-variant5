from django.contrib import admin
from django.urls import path
from mathapp import views as math_views
from guessgame_app import views as guess_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', math_views.index, name='index'),

    path('quadratic/', math_views.quadratic_view, name='quadratic'),

    path('guess/', guess_views.guess_view, name='guess'),
    path('guess/submit/', guess_views.guess_submit, name='guess_submit'),
]