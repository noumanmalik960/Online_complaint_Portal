from django.urls import path, include


app_name = 'users'
urlpatterns = [
    # Default auth urls for login and logout
    path('', include('django.contrib.auth.urls')),
    
]
