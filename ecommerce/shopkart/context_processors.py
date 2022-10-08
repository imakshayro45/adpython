from . models import Category

def menu_links(request):
    QQ=Category.objects.all()
    return dict(links=QQ)
