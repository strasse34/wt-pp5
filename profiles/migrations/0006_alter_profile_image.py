# Generated by Django 3.2.23 on 2023-11-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../uc17ao5y4hftdcoz8kjq', upload_to='images/pp5-wt/'),
        ),
    ]
