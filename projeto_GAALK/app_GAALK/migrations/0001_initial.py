# Generated by Django 4.2.6 on 2023-11-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.IntegerField(unique='')),
                ('email', models.EmailField(max_length=254, unique='')),
                ('senha', models.CharField(max_length=30)),
                ('conf_senha', models.CharField(max_length=30)),
            ],
        ),
    ]
