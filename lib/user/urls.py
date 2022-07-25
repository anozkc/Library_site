from django.urls import path
from user import views


urlpatterns = [
    path('',views.dashboard),
    path('login/',views.login_user),
    path('register/',views.register_user), 
    path('about/',views.user_about),
    path('product/',views.user_product)
]

