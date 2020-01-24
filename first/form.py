from django import forms
from .models import *


class UploadImgForm(forms.ModelForm):

    class Meta:
        model = UploadImg
        fields = ['Img', 'upscaling']
