from django.shortcuts import render, get_object_or_404, redirect
from .models import Dog, Owner, Toy
from .forms import DogForm, OwnerForm, ToyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'my_app/home.html')

def index(request):
    dogs = Dog.objects.all()
    return render(request, 'my_app/index.html', {'dogs': dogs})

def detail(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'my_app/detail.html', {'dog': dog})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def create_dog(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DogForm()
    return render(request, 'my_app/dog_form.html', {'form': form})

@login_required
def update_dog(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    if request.method == 'POST':
        form = DogForm(request.POST, instance=dog)
        if form.is_valid():
            form.save()
            return redirect('detail', dog_id=dog.id)
    else:
        form = DogForm(instance=dog)
    return render(request, 'my_app/dog_form.html', {'form': form, 'dog': dog})

@login_required
def delete_dog(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    dog.delete()
    return redirect('index')

@login_required
def owner_index(request):
    owners = Owner.objects.all()
    return render(request, 'my_app/owner_index.html', {'owners': owners})

@login_required
def owner_detail(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'my_app/owner_detail.html', {'owner': owner})

@login_required
def create_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner_index')
    else:
        form = OwnerForm()
    return render(request, 'my_app/owner_form.html', {'form': form})

@login_required
def update_owner(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_detail', owner_id=owner.id)
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'my_app/owner_form.html', {'form': form, 'owner': owner})

@login_required
def delete_owner(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    owner.delete()
    return redirect('owner_index')

@login_required
def toy_index(request):
    toys = Toy.objects.all()
    return render(request, 'my_app/toy_index.html', {'toys': toys})

@login_required
def toy_detail(request, toy_id):
    toy = get_object_or_404(Toy, pk=toy_id)
    return render(request, 'my_app/toy_detail.html', {'toy': toy})

@login_required
def create_toy(request):
    if request.method == 'POST':
        form = ToyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('toy_index')
    else:
        form = ToyForm()
    return render(request, 'my_app/toy_form.html', {'form': form})

@login_required
def update_toy(request, toy_id):
    toy = get_object_or_404(Toy, pk=toy_id)
    if request.method == 'POST':
        form = ToyForm(request.POST, instance=toy)
        if form.is_valid():
            form.save()
            return redirect('toy_detail', toy_id=toy.id)
    else:
        form = ToyForm(instance=toy)
    return render(request, 'my_app/toy_form.html', {'form': form, 'toy': toy})

@login_required
def delete_toy(request, toy_id):
    toy = get_object_or_404(Toy, pk=toy_id)
    toy.delete()
    return redirect('toy_index')
