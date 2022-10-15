from django.contrib import admin
from home.models import Maqola, Certificate, Information, Arxiv, Konferensiya, About, HozirgiSon, Indexing


class MaqolaAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'create_date', 'image_tag']
    readonly_fields = ['create_time', 'create_date', 'image_tag']


class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ['image_tag']


class ArxivAdmin(admin.ModelAdmin):
    list_display = ['maqola_title', 'maqola_id', 'maqola_create_date']


class KonferensiyaAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ['image_tag', 'create_date', 'create_time']


class IndexingAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ['image_tag']


admin.site.register(Indexing, IndexingAdmin)
admin.site.register(HozirgiSon)
admin.site.register(About)
admin.site.register(Konferensiya, KonferensiyaAdmin)
admin.site.register(Information)
admin.site.register(Arxiv, ArxivAdmin)
admin.site.register(Maqola, MaqolaAdmin)
admin.site.register(Certificate, CertificateAdmin)
