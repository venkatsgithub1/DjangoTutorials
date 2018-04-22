from django.shortcuts import render
# importing http response to create a response.
from django.http import HttpResponse

# every view method needs to have access to
# request and it will be passed using method argument.
def index(request):
    # return a response.
    return HttpResponse("Hello World!!!")