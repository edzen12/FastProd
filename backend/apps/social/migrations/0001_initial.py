# Generated by Django 3.1.7 on 2021-03-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255, verbose_name='Ссылка на соц.сеть')),
                ('image_icon', models.ImageField(help_text='можно взять из сайта  https://www.flaticon.com/', upload_to='social/', verbose_name='Фото иконка соц.сети')),
            ],
            options={
                'verbose_name_plural': 'Соц.сети',
            },
        ),
    ]
