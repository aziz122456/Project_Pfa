# Generated by Django 4.1.6 on 2023-06-11 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reparation_Machine', '0006_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reparation_Machine.machine'),
        ),
    ]