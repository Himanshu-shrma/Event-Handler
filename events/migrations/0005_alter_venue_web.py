# Generated by Django 4.0.3 on 2022-04-12 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.CharField(blank=True, max_length=25, verbose_name='Website Address '),
        ),
    ]