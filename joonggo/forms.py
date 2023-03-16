from django import forms
from .models import Sell, Comment


class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ['subject', 'content', 'price', 'tmethod', 'category', 'images']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']