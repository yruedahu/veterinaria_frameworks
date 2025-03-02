from django.http import HttpResponse

def clinic_home(request):
    return HttpResponse("¡Veterinary Clinic está funcionando!")