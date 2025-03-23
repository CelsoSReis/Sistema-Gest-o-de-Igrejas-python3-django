from .models import Igreja

def logo_igreja(request):
    if request.user.is_authenticated:
        igreja = Igreja.objects.filter(pastor=request.user).first()
        return {"logo_igreja": igreja.logo.url if igreja and igreja.logo else None}
    return {"logo_igreja": None}
