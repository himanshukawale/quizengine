# Generated by Django 3.1.5 on 2021-08-02 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210802_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Questio_text',
            new_name='Question_text',
        ),
    ]
