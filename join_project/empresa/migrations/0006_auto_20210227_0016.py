# Generated by Django 3.1.7 on 2021-02-27 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_auto_20210226_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_permissao', models.CharField(max_length=50, verbose_name='Nome da permissão')),
            ],
            options={
                'verbose_name': 'permissão',
                'verbose_name_plural': '5. Permissões',
            },
        ),
        migrations.AddField(
            model_name='funcionarios',
            name='permissoes',
            field=models.ManyToManyField(blank=True, null=True, to='empresa.Permissoes', verbose_name='Permissões'),
        ),
    ]
