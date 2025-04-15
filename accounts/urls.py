from django.urls import path
from .views import LoginView, RegisterView, EditarCardView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]

urlpatterns += [
    path('editar-card/', EditarCardView.as_view(), name='editar-card'),
]
