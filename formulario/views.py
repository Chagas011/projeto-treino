from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from formulario.forms import RegisterForm

# Create your views here.


def formulario(request):
    register_form_data = request.session.get('register_form_data')

    forms = RegisterForm(register_form_data)
    return render(request, 'formulario/pages/formulario.html', context={
        'form': forms
    })


def valida_formulario(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Your user is created, plese log in.')

        del(request.session['register_form_data'])

    return redirect('forms:formulario')
