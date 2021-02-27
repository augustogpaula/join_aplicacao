# Generated by Django 3.1.7 on 2021-02-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0008_auto_20210227_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alvos',
            options={'verbose_name': 'alvo', 'verbose_name_plural': '6. Alvos'},
        ),
        migrations.AddField(
            model_name='alvos',
            name='deletado',
            field=models.BooleanField(default=False, verbose_name='Deletado ?'),
        ),
        migrations.AlterField(
            model_name='solicitacoes',
            name='resolvido',
            field=models.BooleanField(default=False, verbose_name='Solicitação resolvida ?'),
        ),
    ]