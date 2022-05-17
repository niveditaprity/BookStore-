# Generated by Django 4.0.4 on 2022-05-15 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_review_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book_id',
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
