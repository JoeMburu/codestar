from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic
from .models import Post

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

    return render(
        request, 
        'blog/post_detail.html', 
        { "post": post },
    )