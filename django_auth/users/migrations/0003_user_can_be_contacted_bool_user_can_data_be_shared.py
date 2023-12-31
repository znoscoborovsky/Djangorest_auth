# Generated by Django 4.2.4 on 2023-08-31 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_can_data_be_shared_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="can_be_contacted_bool",
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="can_data_be_shared",
            field=models.CharField(
                blank=True,
                max_length=3,
                verbose_name="voulez-vous partager vos données? oui/non",
            ),
        ),
    ]
