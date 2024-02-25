from django.urls import path

from apps.gap.views import RoomListView, RoomDetailView, LikeOpinionView, CommentView, Loginview, UserRegisterView, \
    UserLogoutView

app_name = 'gap'
urlpatterns = [
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('room/<pk>', RoomDetailView.as_view(), name='room'),
    path('like/<pk>', LikeOpinionView.as_view(), name='opinion-like'),
    path('comment', CommentView.as_view(), name='comment'),
    path('login/', Loginview.as_view(), name='login-page'),
    path('register/', UserRegisterView.as_view(), name='register-page'),
    path('logout/', UserLogoutView.as_view(), name="logout"),

]
