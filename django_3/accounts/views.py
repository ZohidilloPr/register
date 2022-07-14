from django.shortcuts import redirect, render
from .forms import NewUserForm

# Create your views here.

def CreateUser(request):
    form = NewUserForm
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:BV")
    context = {
        "form":form,
    }
    return render(request, "register/signup.html", context)
        