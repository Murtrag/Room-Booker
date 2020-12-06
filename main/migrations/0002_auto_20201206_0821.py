# Generated by Django 2.2 on 2020-12-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='client',
            field=models.CharField(default='me', help_text='Name and Last name of the client who is making this order', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='images',
            field=models.ManyToManyField(to='main.Image'),
        ),
    ]
