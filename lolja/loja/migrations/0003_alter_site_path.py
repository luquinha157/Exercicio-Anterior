# Generated by Django 4.2.4 on 2023-08-29 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_rename_nome_card_site_nome_produto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='path',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
