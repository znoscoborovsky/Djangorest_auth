# Generated by Django 4.2.4 on 2023-08-31 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="can_data_be_shared",
        ),
        migrations.AddField(
            model_name="user",
            name="can_data_be_shared_bool",
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="can_be_contacted",
            field=models.CharField(
                blank=True,
                max_length=3,
                verbose_name="voulez-vous être contacté? oui/non",
            ),
        ),
    ]
