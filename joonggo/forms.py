from django import forms
from joonggo.models import Sell, Comment
from django.contrib.auth.models import User

class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ['subject', 'content']
        lables = {
            'subject': '제목',
            'content': '내용',
        }

        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows':10}),   
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
        'content': '댓글내용',
        }