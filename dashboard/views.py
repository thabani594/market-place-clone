from django.contrib.auth.decorators import login_required

from django.shortcuts import render,get_object_or_404

from items.models import Item,Category



@login_required
def index(request):
    Items = Item.objects.filter(created_by = request.user)
    categories = Category.objects.all()

    return render(request , 'dashboard/index.html',{
        'items':Items,
        'categories':categories,
    })


