# Generated by Django 2.2.5 on 2019-09-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotion_identify', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadVoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(upload_to='speech/')),
            ],
        ),
        migrations.DeleteModel(
            name='SharedImage',
        ),
    ]
