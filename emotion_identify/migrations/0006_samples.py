# Generated by Django 2.2.5 on 2019-09-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotion_identify', '0005_uploadvoice_emotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Samples',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(default='NA', max_length=600)),
                ('emotion', models.CharField(default='NA', max_length=100)),
                ('audio', models.FileField(upload_to='sample/')),
            ],
        ),
    ]
