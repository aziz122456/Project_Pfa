# Generated by Django 4.1.6 on 2023-06-10 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reparation_Machine', '0003_alter_ticket_closedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='machine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Reparation_Machine.machine'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='technicien',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets_technicien', to=settings.AUTH_USER_MODEL),
        ),
    ]