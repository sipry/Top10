from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import List, Item, Theme

# Create your views here.


# @login_required
# def create_list.html(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated '
#                                         'successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})


@login_required
def my_lists(request):
    lists = request.user.list_set.all()
    return render(request, 'lists/my-lists.html', {'lists': lists})


@login_required
def create_list(request):
    themes = Theme.objects.all()
    items = Item.objects.all()
    theme = None
    if request.method == 'POST':
        theme = request.POST.get('themes_selector')
        item_list = request.POST.get('item_list')


    return render(request, 'lists/create-list.html', {'themes': themes, 'items': items, 'theme': theme})
