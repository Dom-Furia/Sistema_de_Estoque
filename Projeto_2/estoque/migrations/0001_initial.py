# Generated by Django 5.0.2 on 2024-02-24 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.FloatField()),
                ('Quantidade', models.IntegerField()),
                ('descrição', models.CharField(max_length=200)),
            ],
        ),
    ]
