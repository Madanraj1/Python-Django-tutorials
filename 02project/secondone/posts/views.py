from django.http import HttpResponse

def posts(request):
    return HttpResponse("Hey there this is my posts page HELLO WORLD")
