from home.models import Maqola, Certificate, Information, Arxiv, Indexing


def components(request):
    maqola_all = Maqola.objects.all().order_by('-id')
    certificate = Certificate.objects.all().order_by('-id')[:1]
    information = Information.objects.all().order_by('id')[:5]
    indexing = Indexing.objects.all().order_by('id')[:15]
    context = {
        'maqola_all': maqola_all,
        'certificate': certificate,
        'information': information,
        'indexing': indexing,
    }
    return context
