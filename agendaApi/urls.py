from django.urls import path
from . import views

urlpatterns = [
    path('',views.ContactList, name='home'),
    path('delete/<str:pk>',views.ContactDelete),
    path('create/',views.ContactCreate),
    path('create/done', views.ContactCreatePOST),
    path('update/<str:pk>', views.ContactUpdate),
    path('update/<str:pk>/done', views.ContactUpdatePOST),
]