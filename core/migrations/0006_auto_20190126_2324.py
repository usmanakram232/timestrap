# Generated by Django 2.1.5 on 2019-01-27 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190120_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entries', to='core.Task'),
        ),
    ]
