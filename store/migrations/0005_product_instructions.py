# Generated by Django 5.2.3 on 2025-06-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_benefits_product_image_2_product_image_3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
