# Generated by Django 4.2.4 on 2023-08-29 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='nome_card',
            new_name='nome_produto',
        ),
        migrations.RemoveField(
            model_name='site',
            name='alunos',
        ),
        migrations.RemoveField(
            model_name='site',
            name='primeiro_texto',
        ),
        migrations.RemoveField(
            model_name='site',
            name='segundo_texto',
        ),
        migrations.AddField(
            model_name='site',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='site',
            name='path',
            field=models.ImageField(upload_to=''),
        ),
    ]
