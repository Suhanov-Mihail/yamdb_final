from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (APIGetToken, APISignUp, CategoriesViewSet, CommentViewSet,
                    GenresViewSet, ReviewViewSet, TitleViewSet, UserViewSet)

router = DefaultRouter()
router.register(r'titles', TitleViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'genres', GenresViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                r'/comments', CommentViewSet, basename='comments')
router.register(r'users', UserViewSet)

auth = [
    path('auth/token/', APIGetToken.as_view(), name='get_token'),
    path('auth/signup/', APISignUp.as_view(), name='signup')
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(auth)),
]
