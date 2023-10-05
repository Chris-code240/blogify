from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,FileResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserSerializer, CommentSerializer, BlogPostSerializer,BlogPost,Comment
from .models import ImageProfile
from django.db.models import Q
from random import randint
import re
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def check_token(req):
#     return True
@api_view(['GET'])
def home(request):
    token_param = request.GET.get('token')
    context = {"title":"Blog App","side":True,"search":True,"user":False,"post":None,"login":False,"addBtn":False}
    if token_param:
        try:
            token = Token.objects.get(key=token_param)
            context['user'] = True
            context['login'] = False
            context['addBtn'] = True
        except Token.DoesNotExist:
            context['user'] = False
            context['login'] = True
    else:
        context['user'] = False
        context['login'] = True
    post = BlogPost.objects.all()[0] if not request.GET.get('post_id') else BlogPost.objects.get(id=request.GET.get('post_id'))
    comments = Comment.objects.filter(post=post).all()
    context['post'] = post
    context['comments'] = comments if len(comments) > 0 else False

    author = User.objects.get(id=post.author.id)
    posts_by_author = BlogPost.objects.filter(author=author).all()
    author_profile = ImageProfile.objects.get(user=author)
    context['author'] = author
    context['posts_by_author'] = posts_by_author
    context['profile'] = author_profile
    print(context)
    return render(request,template_name='home.html',context=context)

@api_view(['GET'])
def login(req):
    return render(req,template_name='login.html',context={"title":"Login","side":False,"search":False,"user":False,"login":False})

@api_view(['GET'])
def authorized_login(req):
    token = req.GET.get('token') or None
    if token is None:
        return  render(req,template_name='home.html',context={"title":"Home","side":True,"search":True,"user":False,"login":True})
    user = Token.objects.get(key=token)
    post = BlogPost.objects.get()
    return render(req,template_name='home.html',context={"title":"Home","side":True,"search":True,"user":True,"addBtn":True,"token":token})

@api_view(['POST'])
def addPost(request):
    print(request.data)
    try:
        data = request.data
        token = Token.objects.get(key=data['token'])
        user = token.user
        post = BlogPost(text=data.get('text'),author=user,image=request.FILES.get('image'),title=data.get('title'))
        post.save()
        return Response({"success":True},status=status.HTTP_200_OK)
    except Token.DoesNotExist:
        return Response({"message": "User not Authorzied"},status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def delete_post(req):
    post = BlogPost.objects.all()
    post.delete()
    return Response({"message":"Post Deleted"})

@api_view(['GET'])
def render_image(request):
    post = BlogPost.objects.get(id=request.GET.get('image_id'))
    print(post.image)
    if post.image:
        path = post.image.url
        return HttpResponse(path)
    return Response({"message":"None"})
@api_view(['POST'])
def login_user(request):
    try:
        is_email = re.match(r'^[\w\.-]+@[\w\.-]+$',request.data['id'])
        if is_email:
            user = User.objects.get(email=request.data['id'])
        else:
            user = User.objects.get(username=request.data['id'])
        
        if user and user.check_password(request.data['password']):
            token,created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key},status=status.HTTP_200_OK)
        return Response({"success":False,"message":"User not Found"},status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({"success":False,"message":str(e)},status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def register_user(req):
    try:
        data = req.data
        next = req.POST.get('next')
        user = User(username=data['username'],first_name=data['first_name'],last_name=data['last_name'],email=data['email'],password=data['password'])
        user.save()
        user.set_password(data['password'])
        user.save()
        image_profile = ImageProfile(user=user,image=req.FILES.get('profile-image'))
        image_profile.save()
        token = Token.objects.create(user=user)
        
        return Response({"success":True,"token":token.key,"next":next},status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e))        

@api_view(['POST'])
def post_comment(request):
    # text = CharField(max_length=1000)
    # post = OneToOneField(BlogPost,on_delete=CASCADE)
    # user = ForeignKey(User,on_delete=CASCADE)
    print(request.data)
    try: 
        token = Token.objects.get(key=request.data['token'])
    except Token.DoesNotExist:
            return Response({"message":"User Does Not Exist","logged_in":False},status=status.HTTP_404_NOT_FOUND)
    user = token.user
    post = BlogPost.objects.get(id=request.data['post_id'])

    if not post:
        return Response({"message":"Blog Post Does Not Exist"},status=status.HTTP_404_NOT_FOUND)
    comment = Comment(user=user,text=request.data['text'],post=post)
    comment.save()
    return Response({"success":True,"comment_id":comment.id},status=status.HTTP_200_OK)

@api_view(['POST'])
def refresh_comment(request):
    print(request.data)
    try:
        comment = Comment.objects.get(id=request.data['comment_id'])
        if not comment:
            return Response({"message":"Comment Does Not exist"},status=status.HTTP_404_NOT_FOUND)
        return Response({"comment":comment.text,"username":comment.user.username})
    except Exception as e:
        print(e)
        return Response({"message":str(e)})

@api_view(['POST'])
def delete_user(req):
    user = User.objects.all()
    user.delete()
    return Response({"message":"User Deleted"})    

@api_view(['GET'])
def render_addPost(request):
    token_param = request.GET.get('token')
    context = {"title":"Blog App","side":True,"search":True,"user":False,"post":None,"login":False,"addBtn":False}
    if token_param:
        try:
            token = Token.objects.get(key=token_param)
            context['user'] = True
            context['login'] = False
            author = token.user
            profile = ImageProfile.objects.get(user=author)
            context['author'] = author
            context['profile'] = profile
        except Token.DoesNotExist:
            context['user'] = False
            context['login'] = True
    else:
        context['user'] = False
        context['login'] = True
        context['side'] = False

    print(context)
    return render(request,template_name="addPost.html",context=context)


@api_view(['POST'])
def search(request):
    try:
        posts = BlogPost.objects.filter(title__icontains=request.data['term']).all()
        posts = [{"title":p.title,"content":p.get_some_words(),"image":p.image.url,"id":p.id} for p in posts]
        return JsonResponse(posts,safe=False)
    except Exception as e:
        return Response({"message":str(e)})
    

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def verify_token(req):
    return Response({"message":"Passed","success":True})
# Create your views here.
