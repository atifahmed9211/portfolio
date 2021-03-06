# Generated by Django 2.2.19 on 2021-03-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField()),
                ('text_body', models.TextField()),
                ('post_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
