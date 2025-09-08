from django.shortcuts import render
import base64
from django.http import HttpResponse
from .models import UserImages
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.http import JsonResponse



# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        face_img_data=request.POST['face_image']
        print(face_img_data)
        face_img_data=face_img_data.split(',')[1]
        face_image=ContentFile(base64.b64decode(face_img_data),name=f"{username}_face.png")
        print(face_image)
        
        try:
            user=User.objects.create(username=username)
        except Exception as e:
            return JsonResponse({'status':'error','message':'User already exists'})
        UserImages.objects.create(user=user,face_image=face_image)
        return JsonResponse({'status':'success','message':'User registered successfully'})


    return render(request, 'register.html')
 