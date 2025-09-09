from django.shortcuts import render
import base64
from django.http import HttpResponse
from .models import UserImages
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.http import JsonResponse
import face_recognition



# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        face_img_data=request.POST['face_image']
        print(face_img_data)
        face_img_data=face_img_data.split(',')[1]
        face_image=ContentFile(base64.b64decode(face_img_data),name=f"{username}_face.jpg")
        print(face_image)
        
        try:
            user=User.objects.create(username=username)
        except Exception as e:
            return JsonResponse({'status':'error','message':'User already exists'})
        UserImages.objects.create(user=user,face_image=face_image)
        return JsonResponse({'status':'success','message':'User registered successfully'})


    return render(request, 'register.html')
 

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        face_img_data=request.POST['face_image']

        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'status':'error','message':'User does not exist'})
        face_image_data=face_img_data.split(',')[1]
        uploaded_image=ContentFile(base64.b64decode(face_image_data),name=f"{username}_face.jpg")

        uploaded_face_image=face_recognition.load_image_file(uploaded_image)
        uploaded_face_encoding=face_recognition.face_encodings(uploaded_face_image)

        if uploaded_face_encoding:
            uploaded_face_encoding=uploaded_face_encoding[0]
            user_image=UserImages.objects.filter(user=user).last()
            stored_face_image=face_recognition.load_image_file(user_image.face_image.path)
            stored_face_encoding=face_recognition.face_encodings(stored_face_image)[0]

            match=face_recognition.compare_faces([stored_face_encoding],uploaded_face_encoding)

            print(match)
        
        return JsonResponse({'status':'success','message':'Login successful' if match[0] else 'Login failed'})

        

    return render(request, 'login.html')