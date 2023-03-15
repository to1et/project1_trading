from django.shortcuts import render, get_object_or_404
from ..models import Sell
from django.db.models import Q


from django.core.paginator import Paginator


# Create your views here.

def index(request):
    """
    joonggo 목록 출력
    """

    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    
    sell_list = Sell.objects.order_by('-create_date')
    if kw:
        sell_list = sell_list.filter(
            Q(subject__icontains=kw) | #제목 검색
            Q(content__icontains=kw) | #내용 검색
            Q(author__username__icontains=kw)
        ).distinct()
        print('===========>', kw)
        print(sell_list[0].content)

   
    paginator = Paginator(sell_list, 12)
    page_obj = paginator.get_page(page)

    context = {'sell_list': page_obj,
               'page': page,
               'kw': kw
               }

    return render(request, 'joonggo/sell_list.html', context)

    
def detail(request,sell_id):
    """
    joonggo 내용 출력
    """
    sell = get_object_or_404(Sell, pk=sell_id)
    context = {'sell': sell}
    return render(request, 'joonggo/sell_detail.html', context)
