from django.urls import path
from . import views

application = 'tutorial'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('foo/', views.FooView.as_view(), name='foo'),
    path('bar/<int:pk>/', views.BarView.as_view(), name='bar'),
]
