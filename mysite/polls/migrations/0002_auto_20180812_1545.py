# Generated by Django 2.0.4 on 2018-08-12 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='coice_text',
            new_name='choice_text',
        ),
    ]
