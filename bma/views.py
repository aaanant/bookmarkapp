from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark 

# Create your views here.
def bookmark_list (request):
	bookmarks = Bookmark.public.all()
	context = {'bookmarks': bookmarks}
	return render(request, 'bma/bookmark_list.html',context)
def bookmark_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        bookmarks = user.bookmarks.all()
    else:
        bookmarks = Bookmark.public.filter(owner__username=username)
    context = {'bookmarks': bookmarks, 'owner': user}
    return render(request, 'bma/bookmark_user.html', context)
