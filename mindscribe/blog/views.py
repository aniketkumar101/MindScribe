from .models import Blog
from .forms import BlogForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            # return redirect('login')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('blog_list')

    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    # return render(request, 'blog_list.html', {'blogs': blogs})  

    # Pagination: 12 blogs per page
    paginator = Paginator(blogs, 12)
    page_number = request.GET.get('page')  # get the page number from URL
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog_list.html', {'page_obj': page_obj})

@login_required
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})



@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form})




@login_required
def blog_edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user = request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_form.html', {'form': form})    



@login_required
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user = request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog_confirm_delete.html', {'blog': blog})

# @login_required
# def blog_like(request, blog_id):
#     blog = get_object_or_404(Blog, pk=blog_id)
#     # Implement like functionality here
#     # For example, you might have a ManyToManyField for likes
#     # blog.likes.add(request.user)
#     return redirect('blog_list')
    

# @login_required
# def blog_comment(request, blog_id):
#     blog = get_object_or_404(Blog, pk=blog_id)
#     if request.method == 'POST':
#         # Handle comment submission
#         pass
#     return redirect('blog_list')
