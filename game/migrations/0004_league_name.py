# Generated by Django 4.1.3 on 2022-12-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_league_language_alter_word_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='name',
            field=models.CharField(default='us', max_length=100),
            preserve_default=False,
        ),
    ]
