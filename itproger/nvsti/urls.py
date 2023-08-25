from django.urls import path
from . import views

urlpatterns = [
    path('', views.nvsti_home, name='nvsti_home'),
    path('<int:pk>', views.NewsDetailView_nv.as_view(), name='nvsti-detailnv'),
]
