from django.shortcuts import render

# Create your views here.
def login_view(request):
    template_view="loggin.html"
    
    
    
    return render(request,template_name=template_view)