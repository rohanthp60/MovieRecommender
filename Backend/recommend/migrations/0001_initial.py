# Generated by Django 5.1.2 on 2024-11-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movies",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=255, unique=True)),
                ("value1", models.IntegerField()),
                ("value2", models.IntegerField()),
                ("value3", models.IntegerField()),
                ("value4", models.IntegerField()),
                ("value5", models.IntegerField()),
            ],
        ),
    ]
