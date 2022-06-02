# Generated by Django 3.2 on 2022-06-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnexoUsuarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.FileField(upload_to='soporte/')),
                ('comentario', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Anexo usuario',
                'verbose_name_plural': 'Anexo usuarios',
                'db_table': 'anexo_usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AnexoVotanteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.FileField(upload_to='soporte/')),
                ('comentario', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Anexo votante',
                'verbose_name_plural': 'Anexo votantes',
                'db_table': 'anexo_votante',
                'managed': True,
            },
        ),
    ]
