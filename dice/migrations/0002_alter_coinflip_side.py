# Generated by Django 5.0.3 on 2024-03-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinflip',
            name='side',
            field=models.CharField(choices=[('H', 'Head'), ('T', 'Tail')], max_length=1),
        ),
    ]
