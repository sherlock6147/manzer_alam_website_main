# Generated by Django 4.2.3 on 2023-08-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("works", "0005_work_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="work",
            name="heroImage",
            field=models.ImageField(blank=True, null=True, upload_to="heroImages/", verbose_name="Hero Image"),
        ),
    ]
