# Generated by Django 3.2 on 2022-06-02 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campana', '0001_initial'),
        ('config', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VotanteModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nodocumento', models.BigIntegerField(db_column='nodocumento', unique=True)),
                ('nombre', models.CharField(db_column='nombre', max_length=45)),
                ('apellido', models.CharField(db_column='apellido', max_length=45)),
                ('movil', models.IntegerField(blank=True, db_column='movil', null=True)),
                ('fijo', models.IntegerField(blank=True, db_column='fijo', null=True)),
                ('direccion', models.CharField(db_column='direccion', max_length=70)),
                ('firma', models.FileField(blank=True, null=True, upload_to='soporte/')),
                ('campana', models.ForeignKey(db_column='campana', on_delete=django.db.models.deletion.DO_NOTHING, to='campana.campanamodel')),
                ('ciudad', models.ForeignKey(db_column='ciudad', on_delete=django.db.models.deletion.DO_NOTHING, to='config.ciudadmodel')),
                ('departamento', models.ForeignKey(db_column='departamento', on_delete=django.db.models.deletion.DO_NOTHING, to='config.departamentomodel')),
                ('estado_usuario', models.ForeignKey(db_column='estado_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='config.estadousuariomodel')),
                ('genero', models.ForeignKey(db_column='genero', on_delete=django.db.models.deletion.DO_NOTHING, to='config.generomodel')),
                ('tipo_documento', models.ForeignKey(db_column='tipo_documento', on_delete=django.db.models.deletion.DO_NOTHING, to='config.tipodocumentomodel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Votante',
                'verbose_name_plural': 'Votantes',
                'db_table': 'votante',
                'managed': True,
            },
        ),
    ]