# Generated by Django 4.1.2 on 2022-10-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_maqola_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='maqola',
            name='doi_link',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
