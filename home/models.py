from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class Maqola(models.Model):
    title = models.TextField(max_length=500)
    author = models.CharField(max_length=600, blank=True, null=True)
    doi_link = models.CharField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to='images/maqola/', default='images/default/default.jpg',
                              db_column="Upload an Image", null=True, blank=True)

    pdf_file = models.FileField(upload_to='pdf/maqola/')

    create_time = models.TimeField(auto_now=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqola'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class Certificate(models.Model):
    title = models.CharField(max_length=300, default='Sertifikat', blank=True, null=True)
    image = models.ImageField(upload_to='images/certificate/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sertifikat'
        verbose_name_plural = 'Sertifikat'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))


class Information(models.Model):
    title = models.TextField(max_length=500)
    link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Information'
        verbose_name_plural = 'Information'


class Arxiv(models.Model):
    maqola = models.ForeignKey(Maqola, on_delete=models.CASCADE, related_name='maqola')

    def maqola_title(self):
        return self.maqola.title

    def maqola_create_date(self):
        return self.maqola.create_date

    def maqola_id(self):
        return self.maqola.id

    def __str__(self):
        return self.maqola.title

    class Meta:
        verbose_name = 'Arxiv'
        verbose_name_plural = 'Arxiv'


class Konferensiya(models.Model):
    title = models.TextField(max_length=1000)
    author = models.CharField(max_length=600, blank=True, null=True)
    description = RichTextField()
    doi_link = models.CharField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to='images/konferensiya/')
    pdf_file = models.FileField(upload_to='pdf/konferensiya/')
    create_time = models.TimeField(auto_now=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Konferensiya'
        verbose_name_plural = 'Konferensiya'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))


class About(models.Model):
    title = models.TextField(max_length=1000)
    sub_title = models.TextField(max_length=1000, blank=True)
    content = RichTextField()

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class HozirgiSon(models.Model):
    title = models.TextField(max_length=1001)
    author = models.CharField(max_length=600, blank=True, null=True)
    description = RichTextField()
    doi_link = models.CharField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to='images/hozirgison/')
    pdf_file = models.FileField(upload_to='pdf/hozirgison/')
    create_time = models.TimeField(auto_now=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hozirgi Son'
        verbose_name_plural = 'Hozirgi Son'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))


class Indexing(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/indexing/')
    link = models.CharField(max_length=3000, blank=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    class Meta:
        verbose_name = 'Indexing'
        verbose_name_plural = 'Indexing'
