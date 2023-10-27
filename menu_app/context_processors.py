from .models import MenuItem

def menus(request):
    menus = MenuItem.objects.all()
    return {'menus': menus}