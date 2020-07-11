from django import forms
from django.forms import ModelForm
from .models import form


class uploadform(ModelForm):

    class Meta:
        model = form
        fields = ['name', 'email', 'aadhaar', 'char_id', 'in_game', 'image']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'id': "exampleInputEmail1",
                    'placeholder': "Enter name",
                    'name': "name"}),
            'email': forms.EmailInput(
                attrs={
                    'class': "form-control",
                    'id': "exampleInputEmail1",
                    'placeholder': "Enter email",
                    'name': "email"}),
            'aadhaar': forms.NumberInput(
                attrs={
                    'class': "form-control",
                    'id': "exampleInputEmail1",
                    'placeholder': "Enter Aadhaar number",
                    'name': "aadhaar"}),
            'char_id': forms.NumberInput(
                attrs={
                    'class': "form-control",
                    'id': "exampleInputEmail1",
                    'placeholder': "Enter Character Id",
                    'name': "char_id"}),
            'in_game': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'id': "exampleInputEmail1",
                    'placeholder': "Enter IGN",
                    'name': "in_game"}),
            'image': forms.FileInput(
                attrs={
                    'class': "form-control",
                    'id': "exampleInputEmail1",
                    'name': "image"}),
        }
