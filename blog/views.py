from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.contrib import messages

# Create your views here.
class PostList(generic.ListView):
    #queryset = Post.objects.all()
    queryset = Post.objects.all()
    #template_name = 'post_list.html'
    template_name = 'blog/index.html'
    paginate_by = 6
    
    
def post_detail(request, slug):
    """ 
    Displays an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:'blog.Post'.

    **Template:**

     :template: `blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments_based_on_post.all().order_by('-created_on')
    comment_count = post.comments_based_on_post.filter(approved=True).count()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            messages.add_message(
                request, 
                messages.SUCCESS, 
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request, 
        'blog/post_detail.html', 
        { 
            "post": post , 
            "comments": comments,
            "comment_count": comment_count, 
            "comment_form": comment_form,
        },
    )