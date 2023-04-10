from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from .models import Post, Category
from .forms import ContactForm

# Create your views here.


def post_list(request):
    posts = Post.published.all().order_by('-publish')
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


def post_index(request):
    last_posts = Post.published.all().order_by('-publish')[:5]
    local_posts = Post.published.all().order_by(
        '-publish').filter(category__name='Mahalliy')[1:6]
    local_post = Post.published.order_by(
        '-publish').filter(category__name='Mahalliy')[0]
    sport_posts = Post.published.all().order_by(
        '-publish').filter(category__name='Sport')[1:6]
    sport_post = Post.published.order_by(
        '-publish').filter(category__name='Sport')[0]
    tex_posts = Post.published.all().order_by(
        '-publish').filter(category__name='Texnologiya')[1:6]
    tex_post = Post.published.order_by(
        '-publish').filter(category__name='Texnologiya')[0]
    world_posts = Post.published.all().order_by(
        '-publish').filter(category__name='Xorij')[:6]
    categories = Category.objects.all()
    return render(request,
                  'blog/post/index.html',
                  {
                      'last_posts': last_posts,
                      'categories': categories,
                      'local_posts': local_posts,
                      'local_post': local_post,
                      'sport_posts': sport_posts,
                      'sport_post': sport_post,
                      'tex_posts': tex_posts,
                      'tex_post': tex_post,
                      'w_posts': world_posts,
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


def post_detail(request, year, month, day, post):
    post1 = get_object_or_404(Post,
                              status=Post.Status.Published,
                              slug=post,
                              publish__year=year,
                              publish__month=month,
                              publish__day=day
                              )
    return render(request,
                  'blog/post/pages/single_page.html',
                  {
                      'post': post1
                  })


class ContactView(TemplateView):
    form = ContactForm()

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, 'blog/post/pages/contact.html', {
            'form': form
        })

    def post(self, request):
        form = ContactForm(request.POST)
        if form.method == 'POST' and form.is_valid():
            form.save()
        return render(request, 'blog/post/pages/contact.html', {
            'form': form
        })
