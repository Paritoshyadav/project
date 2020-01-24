from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import *
import numpy as np
from PIL import Image
from ISR.models import RDN, RRDN
import random
import base64
from django.conf import settings
import os

# Create your views here.


def index(request):

    if request.method == 'POST':
        form = UploadImgForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('display_images')
    else:
        form = UploadImgForm()
    return render(request, 'home.html', {'form': form})


def display_images(request):

    if request.method == 'GET':

        # getting all the objects of UploadImg.
        Upload = UploadImg.objects.last()
        UploadImgs = Upload.Img.url
        UploadImgs = UploadImgs[1:]
        choice = Upload.upscaling
        print(UploadImgs)
        print(choice)

        try:
            img = super_res(UploadImgs, choice)

        except Exception:
            return render(request, 'success.html',
                          {'err': 'Error with image format'})

        return render(request, 'success.html',
                      {'images': img})


def super_res(img, choice):
    img = Image.open(img)
    lr_img = np.array(img)

    if choice == 'el':
        rdn = RRDN(weights='gans')
    elif choice == 's':
        rdn = RDN(weights='psnr-small')
    elif choice == 'l':
        rdn = RDN(weights='psnr-large')
    else:
        rdn = RDN(weights='noise-cancel')

    sr_img = rdn.predict(lr_img)
    image = Image.fromarray(sr_img)
    print(image)
    n = random.randint(1, 100)
    image_name = f'imagee{n}.png'

    image.save(os.path.join(settings.MEDIA_ROOT,
                            image_name))

    with open(os.path.join(settings.MEDIA_ROOT,
                           image_name), "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    print(image_name)
    return my_string.decode('utf-8')

    print(image_name)

    return image_name


'''



    "data:image/png;base64,{{images}}"



'''
