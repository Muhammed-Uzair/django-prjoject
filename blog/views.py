from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# from .forms import NewCommentForm, PostSearchForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView
# Create your views here.


def home(request):
    all_post = Post.newmanager.all()
    context = {'posts': all_post}
    return render(request, 'posts.html', context)


def categ(request):
    return render(request, 'categries.html')


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'single_page.html', {'post': post,
                                                })


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts':   Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        'category_list': category_list
    }
    return context


def post_search(request):
    form = PostSearchForm()
    search = ''
    results = []
    if 'search' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            results = Post.objects.filter(title__contains=search)
    return render(request, 'search.html', {'form': form,
                                           'q': search,
                                           'results': results})
