from django.shortcuts import render, get_object_or_404, redirect
from ..models import Sell
from django.utils import timezone
from ..forms import SellForm

from django.db.models import Q
from django. contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url='common:login')
def sell_create(request):
    """
    joonggo 글작성
    """
    if request.method == 'POST':
        
        form = SellForm(request.POST)
        if form.is_valid():
            sell = form.save(commit=False)
            sell.author = request.user
            sell.create_date = timezone.now()
            sell.save()
            return redirect('joonggo:index')
    else:
        form = SellForm()
    
    context = {'form': form}
    return render(request, 'joonggo/sell_form.html', context)

@login_required(login_url='common:login')
def sell_modify(request, sell_id):
    """
    joonggo 작성글 수정
    """
    sell = get_object_or_404(Sell, pk=sell_id)
    if request.user != sell.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('joonggo:detail', sell_id=sell.id)

    if request.method == "POST":
        form = SellForm(request.POST, instance=sell)
        if form.is_valid():
            sell = form.save(commit=False)
            sell.author = request.user
            sell.modify_date = timezone.now()
            sell.save()
            return redirect('joonggo:detail', sell_id=sell.id)
    else:
        form = SellForm(instance=sell)

    context = {'form': form}
    return render(request, 'joonggo/sell_form.html', context)

@login_required(login_url='common:login')
def sell_delete(request, sell_id):
    """
    joonggo 작성글 삭제
    """
    sell = get_object_or_404(Sell, pk=sell_id)
    if request.user != sell.author:
        messages.error(request, '글삭제권한이 없습니다')
        return redirect('joonggo:detail', sell_id=sell.id)
    sell.delete()
    return redirect('joonggo:index')


@login_required(login_url='common:login')
def sell_mypost(request, sell_id):
    """
    joonggo 목록 출력
    """
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    
    # sell_list = Sell.objects.order_by('-create_date')
    sell_list = request.user.author_sell.order_by('-create_date')
    if kw:
        sell_list = sell_list.filter(
            Q(subject__icontains=kw) | #제목 검색
            Q(content__icontains=kw) | #내용 검색
            Q(author__username__icontains=kw)
        ).distinct()
   
    paginator = Paginator(sell_list, 12)
    page_obj = paginator.get_page(page)

    context = {'sell_list': page_obj,
               'page': page,
               'kw': kw,
               }
    
    return render(request, 'joonggo/sell_mypost.html', context)

@login_required(login_url='common:login')
def sell_mylike(request, sell_id):
    """
    joonggo 목록 출력
    """
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    
    # sell_list = Sell.objects.order_by('-create_date')
    sell_list = request.user.voter_sell.order_by('-create_date')
    if kw:
        sell_list = sell_list.filter(
            Q(subject__icontains=kw) | #제목 검색
            Q(content__icontains=kw) | #내용 검색
            Q(author__username__icontains=kw)
        ).distinct()
   
    paginator = Paginator(sell_list, 12)
    page_obj = paginator.get_page(page)

    context = {'sell_list': page_obj,
               'page': page,
               'kw': kw,
               }
    
    return render(request, 'joonggo/sell_mylike.html', context)