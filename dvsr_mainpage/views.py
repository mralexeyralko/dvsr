from django.shortcuts import render

def mainpage(request):
    return render(request, 'dvsr_mainpage.html', {})

    