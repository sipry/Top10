from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import List, Item, Theme

# Create your views here.


@login_required
def my_lists(request):
    list = None
    themes = Theme.objects.all()
    theme = None
    if request.method == 'POST':
        theme = int(request.POST.get('themes_selector'))
        list = request.user.list_set.filter(theme__id=theme)
        if len(list):
            list = list[0]
    return render(request, 'lists/my-lists.html', {'list': list, 'themes': themes, 'theme': theme})


@login_required
def create_list(request):
    themes = Theme.objects.all()
    items = Item.objects.all()
    theme = None
    if request.method == 'POST':
        theme = request.POST.get('themes_selector')
        item_list = request.POST.get('item_list')
        if item_list:
            item_list = item_list.split(",")
            item_list = [int(i) for i in item_list]
            t = Theme.objects.get(name=theme)

            list = List.objects.create(name='name', user=request.user, theme=t)
            for i in item_list:
                item = Item.objects.filter(id=i).values('id')
                list.item.add(item)

            list.save()

    return render(request, 'lists/create-list.html', {'themes': themes, 'items': items, 'theme': theme})
