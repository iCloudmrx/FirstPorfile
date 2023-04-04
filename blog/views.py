from django.shortcuts import render
from .models import Post, Category
from .forms import ContactForm

# Create your views here.


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


def post_index(request):
    posts = Post.published.all().values()
    categories = Category.objects.all()
    return render(request,
                  'blog/post/index.html',
                  {
                      'posts': posts,
                      'categories': categories
                  })


def post_contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render(request,
                  'blog/post/pages/contact.html',
                  {
                      'form': form
                  })


def post_404(request):
    return render(request,
                  'blog/post/pages/404.html')
