# Generated by Django 3.2.8 on 2022-01-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0028_request_keycloak_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serviceoffering",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
