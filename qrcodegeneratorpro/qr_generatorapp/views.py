
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import QRCodeData,RegisterData
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import qrcode
from PIL import Image
from io import BytesIO
import base64


def registratonPage(request):
    if request.method=='GET':
        return render(request,'registratonPage.html')

    else:
        fname1=request.POST.get('username')
        email1=request.POST.get('email')
        mobile1=request.POST.get('mobile')
        password1=request.POST.get('password')
        pwd1=request.POST.get('password1')
        if password1==pwd1:
            my_user=User.objects.create_user(username=fname1,email=email1,password=password1)
            my_user.is_staff=True
            my_user.save()

            RegisterData(
            uname=fname1,
            email=email1,
            mobile=mobile1,
            password=password1,
            pwd=pwd1
            ).save()
            messages.success(request,'Registration Successfull,Please Login Here!!!')



        else:
            messages.error(request, 'Password and confirm password must be same')
            # Additional password validation error messages
            return redirect('registratonPage')

        return redirect('loginPage')

def loginPage(request):
    if request.method=='GET':
        return render(request,'loginPage.html')

    else:
        name=request.POST.get('username')
        pw=request.POST.get('password')
        user=authenticate(username=name,password=pw)
        if user is not None:
            login(request, user)
            return redirect('qr_generatorPage')
        else:
            messages.error(request, 'Invalid login credentials. Please try again')
            return redirect('loginPage')


def logoutpage(request):
    logout(request)
    return render(request,'loginPage.html')


@login_required(login_url="loginPage")
def qr_generatorPage(request):
    context = {}
    if request.method == "POST":
        qr_text = request.POST.get("qr_text", "")
        qr_image = qrcode.make(qr_text, box_size=8)
        qr_image_pil = qr_image.get_image()
        stream = BytesIO()
        qr_image_pil.save(stream, format='JPEG')  # Changed from PNG to JPEG
        qr_image_data = stream.getvalue()
        qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
        context['qr_image_base64'] = qr_image_base64
        context['variable'] = qr_text
        # Add a URL for downloading the QR code
        context['download_url'] = f"/download_qr/{qr_text}/"  # Adjust as per your URL configuration


    return render(request, 'qr_generator.html', context=context)

def download_qr(request, text):
    # Generating QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buf = BytesIO()
    img.save(buf, format='PNG')
    image_stream = buf.getvalue()

    # Sending response
    response = HttpResponse(image_stream, content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename={text}.png'
    return response
