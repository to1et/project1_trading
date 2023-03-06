from django.shortcuts import render, get_object_or_404, redirect
from .models import Sell
from django.utils import timezone
from .forms import SellForm, CommentForm
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
    paginator = Paginator(sell_list, 10) # 페이지당 10개씩
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

def sell_create(request):
    """
    joonggo 글작성
    """
    if request.method == 'POST':
        
        form = SellForm(request.POST)
        if form.is_valid():
            sell = form.save(commit=False)
            sell.create_date = timezone.now()
            sell.save()
            return redirect('joonggo:index')
    else:
        form = SellForm()
    
    context = {'form': form}
    return render(request, 'joonggo/sell_form.html', context)

def comment_create(request, sell_id):
    """
    joonggo 댓글등록
    """

    sell = get_object_or_404(Sell, pk=sell_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.sell = sell
            comment.save()
            return redirect('joonggo:detail', sell_id=sell.id)
    else:
        form = CommentForm()
    context = {'sell': sell, 'form': form}    
    return render(request, 'joonggo/sell_detail.html', context)