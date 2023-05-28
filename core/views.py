from django.shortcuts import render

menu = {
    'O NÁS': '/',
    'PODUJATIA': '/',
    'NAŠE AKTIVITY': '',
    'KONTAKT': '',
    'DOKUMENTY': ''
}

def index(request):
    template = 'pages/index.html'
    data = {"title": "Voices of Hope", "menu": menu}
    return render(request, template, context=data)

