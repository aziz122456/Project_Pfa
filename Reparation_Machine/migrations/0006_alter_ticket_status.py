# Generated by Django 4.1.6 on 2023-06-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reparation_Machine', '0005_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Ticket Opened'), ('CLOSED', 'Ticket Closed'), ('IN_PROGRESS', 'Pane Normal')], default='OPEN', max_length=20),
        ),
    ]
