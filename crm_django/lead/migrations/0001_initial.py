# Generated by Django 3.2 on 2022-08-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=12)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('confidence', models.IntegerField(blank=True, null=True)),
                ('estimated_value', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('contacted', 'Contacted'), ('inprogress', 'Inprogress'), ('lost', 'Lost'), ('won', 'Won')], default='new', max_length=255)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
