# Generated by Django 4.1.1 on 2023-03-22 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_user', models.CharField(max_length=200, verbose_name='cuenta')),
                ('password', models.CharField(max_length=200, verbose_name='Password')),
                ('profile', models.CharField(max_length=200, verbose_name='Perfil')),
                ('status', models.BooleanField(max_length=200, verbose_name='Status')),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.datacolaboradores')),
            ],
        ),
    ]
