from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

# create views for guestbook that returns templates.

#returns index template.
def index(request):
    # get comments from the databases.
    # - = reverse chronological order.
    comments = Comment.objects.order_by('-date_added')

    # pass the comments to the template and will be passed to
    # context.
    context = {'comments':comments}
    return render(request, 'guestbook/index.html', context=context)

# returns sign template.
def sign(request):
    
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')
    else:
        # get request.
        # instantiate the form
        form = CommentForm()

    context = {'form':form}
    return render(request, 'guestbook/sign.html', context=context)
