# Generated by Django 4.0.3 on 2022-03-13 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_order_book_order_customer_alter_order_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
