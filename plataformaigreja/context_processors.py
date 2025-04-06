from .models import Membros

def total_membros_context(request):
    if request.user.is_authenticated:
        total_membros = Membros.objects.filter(pastor=request.user).count()
    else:
        total_membros = 0
    return {
        'total_membros': total_membros
    }
