from django.urls import path
from . import views

urlpatterns = [
    path('cvbuilder', views.cvbuilder, name="cvbuilder"),
    # path('generate-pdf/', views.my_view, name='generate_pdf'),
    path('info',views.info,name="info")
]
