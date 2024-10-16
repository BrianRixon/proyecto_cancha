# Generated by Django 5.1.1 on 2024-10-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cancha', '0002_registro_last_login_alter_registro_apellido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('tenis1', 'tenis1'), ('tenis2', 'tenis2'), ('paddle1', 'paddle1'), ('paddle2', 'paddle2'), ('paddle3', 'paddle3'), ('futbol', 'futbol')], max_length=25, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
