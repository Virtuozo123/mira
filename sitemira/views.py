from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import create, Comment
from .forms import create_project, CommentForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,'pages/index.html',{})

def create_page(request):
    if request.method == "POST":
        form = create_project(request.POST, request.FILES)
        if form.is_valid():
            create = form.save(commit=False)
            create.author = request.user
            create.save()
            return redirect('project', pk=create.pk)
    else:
        form = create_project()
    return render(request,'pages/create.html',{'form' : form })

def donation(request):
    creates = create.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'pages/donation.html', {'creates': creates })

def donation_pensioner(request):
    creates = create.objects.filter(chosen_category='Пенсионеры и Инвалиды').order_by('published_date')
    return render(request,'pages/donation.html', {'creates': creates })

def donation_poor(request):
    creates = create.objects.filter(chosen_category='Малоимущие семьи').order_by('published_date')
    return render(request,'pages/donation.html', {'creates': creates })

def donation_child(request):
    creates = create.objects.filter(chosen_category='Больные дети и сироты').order_by('published_date')
    return render(request,'pages/donation.html', {'creates': creates })

def donation_churches(request):
    creates = create.objects.filter(chosen_category='Храмы и монастыри').order_by('published_date')
    return render(request,'pages/donation.html', {'creates': creates })

def donation_prisoners(request):
    creates = create.objects.filter(chosen_category='Заключенные').order_by('published_date')
    return render(request,'pages/donation.html', {'creates': creates })

def donation_mercy(request):
    creates = create.objects.filter(chosen_category='Дома милосердия').order_by('published_date')
    return render(request,'pages/donation.html', {'creates': creates })

def project(request, pk):
    created = get_object_or_404(create, pk=pk)
    return render(request,'pages/project.html',{'created': created })

@login_required
def verifi_list(request):
    creates = create.objects.filter(published_date__isnull=True)
    return render(request,'pages/project_verifi.html', {'creates': creates })

@login_required
def publish_project(request, pk):
    created = get_object_or_404(create, pk=pk)
    created.publish()
    return redirect('project', pk=pk)
@login_required
def delete_project(request, pk):
    created = get_object_or_404(create, pk=pk)
    created.delete()
    return redirect('verifi_list')

class RegisterFormView(FormView):
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "pages/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
    
@login_required   
def add_comment_to_post(request, pk):
    created = get_object_or_404(create, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = created
            comment.save()
            return redirect('project', pk=created.pk)
    else:
        form = CommentForm()
    return render(request, 'pages/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('project', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('project', pk=comment.post.pk)