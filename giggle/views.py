from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .apis import get_giggle_result
from .models import Joke


def giggle_search(request):
    context = {}
    if request.method == 'POST':
        query = request.POST.get('query')
        if len(query) > 50:
            return redirect('giggle_search')
        response = get_giggle_result(query)
        if response == 1:
            messages.error(request, 'You have hit the rate limit of 3 requests per minute, please try again in a moment.')
            return render(request, './giggle/giggle_search.html', context)
        context['query'] = query.capitalize()
        context['response'] = response
        new_joke_object = Joke(query=query, response=response)
        new_joke_object.save() 

    return render(request, './giggle/giggle_search.html', context)


def giggle_history(request):
    jokes = Joke.objects.all().order_by('-created_at')
    paginator = Paginator(jokes, 8)
    page_no = request.GET.get('page', 1)
    curr_page = paginator.get_page(page_no)
    return render(request, './giggle/giggle_history.html', context={'jokes': curr_page})


def delete_joke(request, pk):
    joke_to_delete = get_object_or_404(Joke, pk=pk)
    joke_to_delete.delete()
    return redirect('giggle_history')

