from django.http import HttpResponse

def test(request):
    return HttpResponse("Olá mundo do Django")