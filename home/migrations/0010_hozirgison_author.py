# Generated by Django 4.1.2 on 2022-10-15 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_maqola_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='hozirgison',
            name='author',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]