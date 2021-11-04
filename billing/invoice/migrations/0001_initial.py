# Generated by Django 3.1.7 on 2021-11-04 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha en la que fue creado el registro.', verbose_name='creado en')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha en la que fue modificado el registro.', verbose_name='mmodificado en')),
                ('describe', models.TextField(blank=True, help_text='Descripcion del descuento', null=True, verbose_name='Descripcion')),
                ('discount', models.IntegerField(help_text='Cantidad de productos', verbose_name='Descuento de')),
                ('code', models.CharField(max_length=11, unique=True, verbose_name='Codigo')),
                ('duration', models.DateTimeField(help_text='Fecha en la que fue modificado el registro.', verbose_name='Duracion')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
