from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Category
from .forms import ContactForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


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


@login_required
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
    comments = post1.comments.filter(active=True)
    new_comment = None
    if request.method == "POST":
        comment_form = ContactForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post1
            new_comment.user = request.user
            new_comment.save()
            CommentForm()
    form = CommentForm()
    return render(request,
                  'blog/post/pages/single_page.html',
                  {
                      'post': post1,
                      'comments': comments,
                      'new_comment': new_comment,
                      'comment_form': form
                  })


class ContactView(LoginRequiredMixin, TemplateView):
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


def localView(request):
    posts = Post.published.all().order_by(
        '-publish').filter(category__name='Mahalliy')[:10]
    return render(request, 'blog/post/pages/local.html',
                  {
                      'posts': posts,
                  })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    admin_users = User.objects.filter(is_superuser=True)
    return render(request, 'admin/page.html', {
        'users': admin_users
    })
