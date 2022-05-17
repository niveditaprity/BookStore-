# Generated by Django 4.0.4 on 2022-05-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='longDescription',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='shortDescription',
            field=models.CharField(max_length=218, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='thumbnailUrl',
            field=models.CharField(max_length=218, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pageCount',
            field=models.IntegerField(default=0),
        ),
    ]
