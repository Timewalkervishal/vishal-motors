# Generated by Django 5.1.4 on 2025-01-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superman', '0006_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='discribe',
            field=models.TextField(blank=True, null=True),
        ),
    ]
