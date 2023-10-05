from django.urls import re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    re_path('home/',views.home),
    re_path('auth/',views.login),
    re_path('login/user/',views.login_user),
    re_path('register/user/',views.register_user),
    re_path('delete/',views.delete_user),
    re_path('verify-token/',views.verify_token),
    re_path('verified/login/',views.authorized_login),
    re_path('add-post/',views.addPost),
    re_path('post/image/',views.render_image),
    re_path('delete-post/',views.delete_post),
    re_path('addpost/',views.render_addPost),
    re_path('comment/',views.post_comment),
    re_path('refresh-comments/',views.refresh_comment),
    re_path('posts/search',views.search),
    re_path('post/get/',views.home)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)