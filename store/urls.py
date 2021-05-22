from django.urls import path
from .views import Index,Signup,Login

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',Index.as_view(),name='homepage'),
    path('signup',Signup.as_view()),
    path('login',Login.as_view())
]
