# Generated by Django 2.2.1 on 2019-09-20 10:44

from django.db import migrations, models
import drf_secure_token.abstract_models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_secure_token', '0006_auto_20170227_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='dead_in',
            field=models.DateTimeField(default=drf_secure_token.abstract_models.DyingTokenMixin.default_dead_time),
        ),
        migrations.AlterField(
            model_name='token',
            name='expire_in',
            field=models.DateTimeField(default=drf_secure_token.abstract_models.ExpiredTokenMixin.default_expire_time),
        ),
        migrations.AlterField(
            model_name='token',
            name='key',
            field=models.CharField(blank=True, default=drf_secure_token.abstract_models.BaseToken.generate_key, max_length=40, unique=True),
        ),
    ]
