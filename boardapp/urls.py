from django.urls import path
from .views import signupfunc

# urlpatternsを記述
urlpatterns = [
    # urlはprojectとappどちらも追記する、appは作成しなければいけない
    path('signup/', signupfunc),
]
