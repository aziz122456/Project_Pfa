# Generated by Django 4.1.6 on 2023-06-11 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reparation_Machine', '0007_alter_ticket_machine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Ticket Opened'), ('CLOSED', 'Ticket Closed'), ('IN_PROGRESS', 'ticket in progress')], default='OPEN', max_length=20),
        ),
    ]
