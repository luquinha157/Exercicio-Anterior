# Generated by Django 4.2.4 on 2023-08-30 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_alter_site_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_carousel', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('path', models.ImageField(upload_to='images/')),
                ('classe', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
    ]