# Generated by Django 4.0.4 on 2022-04-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_valoracio_mitja_valoracio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valoracio',
            name='valor',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=0),
        ),
    ]