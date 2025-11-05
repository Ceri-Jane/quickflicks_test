from django.shortcuts import render

def home(request):
    query = request.GET.get('query', '')
    return render(request, 'movies/home.html', {'query': query})