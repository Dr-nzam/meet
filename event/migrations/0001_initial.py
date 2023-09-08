# Generated by Django 4.2.4 on 2023-09-08 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentreInteret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=128)),
                ('image', models.FileField(blank=True, upload_to='assets/cat/')),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomEvent', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=128)),
                ('lieux', models.CharField(max_length=128)),
                ('DateEvent', models.CharField(default=0, max_length=128)),
                ('description', models.TextField()),
                ('image', models.FileField(blank=True, upload_to='assets/images/')),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventcat', to='event.centreinteret')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventgroup', to='group.group')),
            ],
        ),
        migrations.CreateModel(
            name='SousCentreInteret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=128)),
                ('centreInteret', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='souscat', to='event.centreinteret')),
            ],
        ),
        migrations.CreateModel(
            name='Participe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evenement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='event.evenement')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
