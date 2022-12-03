# Generated by Django 4.0.3 on 2022-11-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_alter_order_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, choices=[('pending', 'pending'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered')], null=True),
        ),
    ]
