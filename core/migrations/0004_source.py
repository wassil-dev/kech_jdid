# Generated by Django 3.2.4 on 2021-06-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_publication_date_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('logo', models.CharField(blank=True, max_length=100, null=True, verbose_name='logo')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='link')),
                ('feed_link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Feed link')),
                ('laste_updted', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Source',
            },
        ),
    ]
