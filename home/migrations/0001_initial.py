# Generated by Django 3.2 on 2021-05-26 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keyword', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('fax', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('smptserver', models.CharField(max_length=20)),
                ('smptpassword', models.CharField(max_length=20)),
                ('smptport', models.CharField(blank=True, max_length=5)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('aboutus', models.TextField()),
                ('contact', models.TextField()),
                ('referances', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]