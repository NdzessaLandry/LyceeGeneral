# Generated by Django 5.1.3 on 2024-12-03 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmploiDeTemps', '0006_alter_classeenseignantcours_id_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='classeenseignantcours',
            unique_together={('id_enseignant', 'id_cours')},
        ),
    ]
