# Generated by Django 5.1.3 on 2024-11-18 05:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmploiDeTemps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClasseCours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_classe', models.ForeignKey(db_column='id_classe', on_delete=django.db.models.deletion.DO_NOTHING, to='EmploiDeTemps.classe')),
                ('id_cours', models.ForeignKey(db_column='id_cours', on_delete=django.db.models.deletion.DO_NOTHING, to='EmploiDeTemps.cours')),
            ],
            options={
                'db_table': 'classe_cours',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SallePeriode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_periode', models.ForeignKey(db_column='id_periode', on_delete=django.db.models.deletion.DO_NOTHING, to='EmploiDeTemps.periode')),
                ('id_salle', models.ForeignKey(db_column='id_salle', on_delete=django.db.models.deletion.DO_NOTHING, to='EmploiDeTemps.salle')),
            ],
        ),
    ]