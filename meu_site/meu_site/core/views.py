from django.shortcuts import render
from django.http import JsonResponse
from .rpa.coletor import executar_automacao

def home(request):
    return render(request, 'core/home.html')

def sobre(request):
    return render(request, 'core/sobre.html')

def iniciar_rpa(request):
    if request.method == "POST":
        # recebe a url do formulario
        url = request.POST.get("url", "").strip()
        if not url.startswith("http"):
            url = "https://" + url

        # executa o robo
        resultado = executar_automacao(url)

        # retorna como JSON (para exibir no html)
        return JsonResponse(resultado)
    
    return render(request, 'core/rpa.html')
