# Generated by Django 5.1.3 on 2024-12-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmploiDeTemps', '0005_classeenseignantcours_id_classeperiodecours_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classeenseignantcours',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='classeperiodecours',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]