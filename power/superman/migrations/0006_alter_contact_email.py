# Generated by Django 5.1.4 on 2025-01-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superman', '0005_alter_contact_date_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=122),
        ),
    ]
