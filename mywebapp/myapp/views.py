from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is the landing page")

def test(request):
    return HttpResponse("This is the test page")

def show(request):
    return HttpResponse("Now we have understood the concept of url mapping")


#made by ayush
def dikhrhahai(request):
    return HttpResponse("Mujhe url mapping krna aata hai re bhai apna kaam krlo cllg walon")

