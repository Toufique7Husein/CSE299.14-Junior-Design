# Generated by Django 3.2.5 on 2021-12-16 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='userImage.png', null=True, upload_to=''),
        ),
    ]
