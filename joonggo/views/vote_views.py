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
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    elif sell.voter.filter(pk=request.user.pk).exists(): # 추천을 한 경우 추천수 -1
        sell.voter.remove(request.user)
    else:
        sell.voter.add(request.user) # 추천을 한 적이 없다면 추천수 +1       

    return redirect('joonggo:detail', sell_id=sell.id)