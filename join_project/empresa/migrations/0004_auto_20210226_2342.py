# Generated by Django 3.1.7 on 2021-02-26 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_auto_20210226_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='endereco',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresa.endereco', verbose_name='Endereço'),
        ),
    ]
