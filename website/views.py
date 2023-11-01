from django.shortcuts import render, redirect, get_object_or_404
from . models import TodoList, Managers, Products, Departments, Profile
from django.contrib import messages
import datetime
from .forms import TodoForm, SearchForm, AddProductForm, AddManagerForm, AddDepartmentForm
from django.contrib.auth.models import User
from django.db.models import Sum
from member.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required(redirect_field_name='sign_inn', login_url='sign_inn')
def home(request):
    action = request.POST.get('action')

    # List of all the todos
    todos = TodoList.objects.all()
    # ///////////------------------

    # Total number of todos recorded
    number_todo = TodoList.objects.all().count()
    # //////////-------------------

    # Get current date and time
    date = datetime.date.today
    # /////////--------------------

    # Count the number of users in the db
    users = CustomUser.objects.all().count()
    # ///////--------------------

    # All product reistered
    products = Products.objects.all()
    # ///////--------------------

    # All profiles
    profile = Profile.objects.all()
    # ////////--------------------

    # Sum up prices for all products taken
    amount = Products.objects.aggregate(total=Sum('price'))['total']
    # //////////------------------
    task_by_user = TodoList.objects.filter(user_mail=request.user).count()
    context = {'todos': todos,
               'date': date,
               'users': users,
               'number_todo': number_todo,
               'products': products,
               'amount': amount,
               'profile': profile,
               'task_by_user': task_by_user}

    if request.method == "POST":
        if action == 'search':
            search = request.POST.get('search')
            searched = TodoList.objects.filter(
                name__icontains=search)
        else:
            return render(request, 'chart.html')

        return render(request, 'search.html', {'searched': searched})

    return render(request, 'index.html', context)


# Add new todo
def add_todo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'New item added to your todo list')
            return redirect('/')
    return render(request, 'form.html', {'form': form})


# Edit or update todo
def edit_todo(request, todo_id):
    item = TodoList.objects.get(pk=todo_id)
    form = TodoForm(instance=item)
    if request.method == "POST":
        form = TodoForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task deleted')
            return redirect('/')
    return render(request, 'form.html', {'form': form, })


# Delete todo
def delete_todo(request, todo_id):
    todos = TodoList.objects.get(pk=todo_id)
    todos.delete()
    messages.success(request, 'Task deleted')
    return redirect('/')


def form(request):
    return render(request, 'form.html', {})


def chart_view(request):
    return render(request, 'chart.html')


@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, pk=room_id)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return render(request, 'chat.html', {'room': room, 'messages': messages})


@login_required
def send_message(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(ChatRoom, pk=room_id)
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                room=room, user=request.user, content=content)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})


# Adding products from website
def add_product(request):
    form = AddProductForm()
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added')
        redirect('add-product')
        messages.success(request, 'Something is wrong with your form')
    return render(request, 'product.html', {'form': form})


# Adding managers from website
def add_managers(request):
    form = AddManagerForm()
    if request.method == "POST":
        form = AddManagerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manager added')
        else:
            redirect('home')
            messages.success(request, 'Something is wrong with your form')
    return render(request, 'add_manager.html', {'form': form})


# Adding dpartment from website
def add_department(request):
    form = AddDepartmentForm()
    if request.method == "POST":
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('department')
    return render(request, 'add_department.html', {'form': form})
