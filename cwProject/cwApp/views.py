from django.http import HttpResponse


# display message on default page load (with blank path)
def index(request):
    return HttpResponse("Index Test")

