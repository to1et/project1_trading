from django import forms
from joonggo.models import Sell, Comment
from django.contrib.auth.models import User

class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ['subject', 'content', 'price', 'category', 'tmethod']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']