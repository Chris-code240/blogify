from django.urls import path, path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('auth/',views.login),
    path('login/user/',views.login_user),
    path('register/user/',views.register_user),
    path('delete/',views.delete_user),
    path('verify-token/',views.verify_token),
    path('verified/login/',views.authorized_login),
    path('add-post/',views.addPost),
    path('post/image/',views.render_image),
    path('delete-post/',views.delete_post),
    path('addpost/',views.render_addPost),
    path('comment/',views.post_comment),
    path('refresh-comments/',views.refresh_comment),
    path('posts/search',views.search),
    path('post/get/',views.home)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)