from operator import attrgetter
from django.shortcuts import render, redirect
from home.models import Maqola, Certificate, Information, Arxiv, Konferensiya, About, HozirgiSon
from home.forms import ContactForm
from contact.models import Contact
from django.contrib import messages
from home.forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import TemplateView, ListView


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    maqola_index = Maqola.objects.all().order_by('-id')[:5]
    certificate = Certificate.objects.all().order_by('-id')[:1]
    information = Information.objects.all().order_by('id')[:5]
    hozirgison = HozirgiSon.objects.all().order_by('-id')

    context = {
        'maqola_index': maqola_index,
        'certificate': certificate,
        'information': information,
        'hozirgison': hozirgison,
    }
    return render(request, 'index/base.html', context)


def contact(request):
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if cform.is_valid():
            data = Contact()
            data.first_name = cform.cleaned_data['first_name']
            data.last_name = cform.cleaned_data['last_name']
            data.email = cform.cleaned_data['email']
            data.phone = cform.cleaned_data['phone']
            data.message = cform.cleaned_data['message']
            data.ip = get_client_ip(request)
            data.save()
            messages.success(request, 'Xabaringiz qabul qilindi! Sizga qisqa fursat ichida javob beramiz. Raxmat!')
            return redirect('contact')
    cform = ContactForm
    context = {
        'cform': cform,
    }
    return render(request, 'contact/base.html', context)


def maqolalar(request):
    maqola_m = Maqola.objects.all().order_by('-id')
    certificate = Certificate.objects.all().order_by('-id')[:1]
    information = Information.objects.all().order_by('id')[:5]

    p = Paginator(maqola_m, 10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    context = {
        'maqola_m': maqola_m,
        'certificate': certificate,
        'information': information,
        'page_obj': page_obj,
    }
    return render(request, 'maqolalar/base.html', context)


def arxiv_view(request):
    maqola_arxiv = Arxiv.objects.all().order_by('-id')
    p = Paginator(maqola_arxiv, 10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {
        'maqola_arxiv': maqola_arxiv,
        'page_obj': page_obj,
    }
    return render(request, 'arxiv/base.html', context)


def konferensiya_view(request):
    konferensiya = Konferensiya.objects.all().order_by('-id')
    context = {
        'konferensiya': konferensiya,
    }
    return render(request, 'konferensiya/base.html', context)


def about_view(request):
    about = About.objects.all().order_by('id')[:15]
    context = {
        'about': about,
    }
    return render(request, 'about/base.html', context)


def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request,
                                 'Muvoffaqiyatli ro`yxatdan o`tildi! Endi yaratgan login va parolingizni kiriting.')
                return redirect('login')
        except:
            messages.error(request, 'Foydalanuvchi nomi yoki email avval ro`yxatdan o`tgan.')
    form = NewUserForm()
    context = {
        'form': form,
    }
    return render(request, 'register/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    form = AuthenticationForm()
    context = {'login_form': form}
    return render(request, 'register/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def get_queryset(request):  # new
    query = request.GET.get("q")
    object_list = Maqola.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    context = {
        'search_result': object_list,
        'q': query,
    }
    return render(request, 'search/base.html', context)
