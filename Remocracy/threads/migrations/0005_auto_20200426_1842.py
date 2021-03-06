# Generated by Django 3.0.5 on 2020-04-26 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('threads', '0004_siteuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='siteUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='threads.SiteUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='siteUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='threads.SiteUser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
