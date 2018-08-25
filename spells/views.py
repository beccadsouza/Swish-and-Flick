from django.shortcuts import render, redirect
from .models import Spell
from django.contrib.auth.decorators import login_required
from . import forms

def spell_list(request):
    spells = Spell.objects.all().order_by('date')
    return render(request, 'spells/spell_list.html',{'spells': spells})

def spell_detail(request, slug):
    spell = Spell.objects.get(slug=slug)
    return render(request, 'spells/spell_detail.html',{'spell': spell})

@login_required(login_url="/#terms1")
def spell_create(request):
    if request.method == 'POST':
        form = forms.CreateSpell(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.contributor = request.user
            instance.save()
            return redirect('spells:list')
    else:
        form = forms.CreateSpell()
    return render(request, 'spells/spell_create.html', { 'form': form})
