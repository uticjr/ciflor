# Generated by Django 2.2.7 on 2019-11-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco_de_vagas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canditato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('emial', models.EmailField(max_length=254)),
                ('curriculo', models.FileField(upload_to='')),
            ],
        ),
    ]
