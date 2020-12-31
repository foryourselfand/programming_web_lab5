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
            dot: Dot = Dot(user=request.user, **form.cleaned_data)
            dot.result = in_area(dot=dot)
            dot.save()
            return redirect('dots:table')
    return render(request, 'dots/create.html', {'form': form})
