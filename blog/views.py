from django.shortcuts import render, get_object_or_404
from .models import Post, Author

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def posts_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)        # get()
    posts = Post.objects.filter(author=author)              # filter()
    all_authors = author.objects.all()                      # all() — наприклад, для меню
    return render(request, 'blog/posts_by_author.html', {
        'author': author,
        'posts': posts,
        'all_authors': all_authors,
    })

# Create your views here.
