from django.urls import path
from .views      import UserView, AuthView, KakaoSignInView

urlpatterns = [
        path('', UserView.as_view()),
        path('/auth', AuthView.as_view()),
        path('/kakao', KakaoSignInView.as_view()),
]
