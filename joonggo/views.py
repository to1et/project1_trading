from django.shortcuts import render
from .models import Sell

# Create your views here.

def index(request):
    """
    joonggo 목록 출력
    """
    sell_list = Sell.objects.order_by('-create_date')
    context = {'sell_list': sell_list}

    return render(request, 'joonggo/sell_list.html', context)

def detail(request,sell_id):
    """
    joonggo 내용 출력
    """
    sell = Sell.objects.get(id=sell_id)
    context = {'sell': sell}
    return render(request, 'joonggo/sell_detail.html', context)