from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Sell


@login_required(login_url='common:login')
def vote_sell(request, sell_id):
    """
    joonggo 작성글 추천
    """
    sell = get_object_or_404(Sell, pk=sell_id)
    if request.user == sell.author:
        messages.error(request, '본인이 작성한 글은 좋아요할 수 없습니다.')
    else:
        sell.voter.add(request.user)
    return redirect('joonggo:detail', sell_id=sell.id)