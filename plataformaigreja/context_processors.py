from .models import Membros

def total_membros_context(request):
    if request.user.is_authenticated:
        total_membros = Membros.objects.filter(pastor=request.user, ativo=True).count()
    else:
        total_membros = 0
    return {
        'total_membros': total_membros
    }

def total_membros_transferidos(request):
    if request.user.is_authenticated:
        total_membros_transf = Membros.objects.filter(pastor=request.user, ativo=False).count()
    else:
        total_membros_transf = 0
    return {
        'total_membros_transf': total_membros_transf
    }
