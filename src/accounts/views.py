from django.shortcuts import render

# Create your views here.
def email_confirm(request):
    return render(request, "success.html")