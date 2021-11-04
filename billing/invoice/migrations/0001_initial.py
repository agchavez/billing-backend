# Generated by Django 3.1.7 on 2021-11-04 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20211103_0315'),
        ('user', '0001_initial'),
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
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha en la que fue creado el registro.', verbose_name='creado en')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha en la que fue modificado el registro.', verbose_name='mmodificado en')),
                ('total', models.FloatField(verbose_name='Total factura: ')),
                ('isv', models.FloatField(verbose_name='ISV 15%')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoicesclient', to='user.client')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoicesdicount', to='invoice.discount')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoicesseller', to='user.seller')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvoicesDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha en la que fue creado el registro.', verbose_name='creado en')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha en la que fue modificado el registro.', verbose_name='mmodificado en')),
                ('total_line', models.FloatField(verbose_name='Total factura: ')),
                ('amount', models.IntegerField(verbose_name='cantidad')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_detail', to='invoice.invoices')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.product')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
