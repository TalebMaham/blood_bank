# Generated by Django 5.1.1 on 2024-09-12 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0002_rename_groupe_sanguin_donateur_gs_rh_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receveur',
            old_name='groupe_sanguin',
            new_name='gs_rh',
        ),
    ]
