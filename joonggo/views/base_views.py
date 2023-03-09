from django.shortcuts import render, get_object_or_404
from ..models import Sell

from django.core.paginator import Paginator

# Create your views here.

def index(request):
    """
    joonggo 목록 출력
    """
    page = request.GET.get('page', '1') # 페이지
    #조회
    sell_list = Sell.objects.order_by('-create_date')
    #페이징 처리
    paginator = Paginator(sell_list, 12) # 페이지당 10개씩
    page_obj = paginator.get_page(page)
    context = {'sell_list': page_obj}

    return render(request, 'joonggo/sell_list.html', context)

def detail(request,sell_id):
    """
    joonggo 내용 출력
    """
    sell = get_object_or_404(Sell, pk=sell_id)
    context = {'sell': sell}
    return render(request, 'joonggo/sell_detail.html', context)
