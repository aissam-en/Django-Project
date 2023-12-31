# Generated by Django 4.2.2 on 2023-06-23 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0008_alter_organisateur_description'),
        ('events_app', '0006_alter_events_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='organisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='users_app.organisateur'),
        ),
    ]
