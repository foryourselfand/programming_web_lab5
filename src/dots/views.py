from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .business import in_area
from .forms import DotCreateForm
from .models import Dot


@login_required(login_url='accounts:login')
def table(request):
    dots = Dot.objects.filter(user=request.user)
    return render(request, 'dots/table.html', {'dots': dots})


@login_required(login_url='accounts:login')
def create(request):
    form = DotCreateForm()
    if request.method == 'POST':
        form = DotCreateForm(request.POST)
        if form.is_valid():
            result: bool = in_area(**form.cleaned_data)
            Dot.objects.create(user=request.user, result=result, **form.cleaned_data)
            return redirect('dots:table')
    return render(request, 'dots/create.html', {'form': form})
