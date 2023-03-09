from django.shortcuts import render, get_object_or_404, redirect
from ..models import Sell, Comment
from django.utils import timezone
from ..forms import CommentForm

from django. contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(login_url='common:login')
def comment_create_sell(request, sell_id):
    """
    joonggo 댓글등록
    """
    sell = get_object_or_404(Sell, pk=sell_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.sell = sell
            comment.save()
            return redirect('joonggo:detail', sell_id=sell.id)
    else:
        form = CommentForm()
    context = {'sell': sell, 'form': form}    
    return render(request, 'joonggo/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_sell(request, comment_id):
    """
    joonggo 질문댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('joonggo:detail', sell_id=comment.sell.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('joonggo:detail', sell_id=comment.sell.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'joonggo/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_sell(request, comment_id):
    """
    joonggo 질문댓글삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('joonggo:detail', sell_id=comment.sell.id)
    else:
        comment.delete()
    return redirect('joonggo:detail', sell_id=comment.sell.id)


