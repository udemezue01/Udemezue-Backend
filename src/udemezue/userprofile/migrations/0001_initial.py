# Generated by Django 3.1.2 on 2021-06-13 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(blank=True, upload_to='')),
                ('bio', models.CharField(blank=True, max_length=3000)),
                ('twitter', models.CharField(blank=True, max_length=3000)),
                ('github', models.CharField(blank=True, max_length=3000)),
                ('facebook', models.CharField(blank=True, max_length=3000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]
