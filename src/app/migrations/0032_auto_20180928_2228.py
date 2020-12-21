# Generated by Django 2.1.1 on 2018-09-28 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20180530_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charityprofile',
            name='charity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Charity'),
        ),
        migrations.AlterField(
            model_name='charityprofile',
            name='cover_image_url',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='charityprofile',
            name='video_url',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ContactCategory'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(max_length=1000, verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='marketingpreference',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='race',
            name='race_year',
            field=models.CharField(max_length=10, verbose_name='Race year'),
        ),
        migrations.AlterField(
            model_name='racesponsor',
            name='race',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Race'),
        ),
        migrations.AlterField(
            model_name='racesponsor',
            name='sponsor_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.SponsorProfile'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='enabled',
            field=models.BooleanField(default=False, verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='logo_url',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='sponsorship_amount',
            field=models.PositiveIntegerField(default=0, verbose_name='Sponsorship Amount'),
        ),
        migrations.AlterField(
            model_name='sponsorprofile',
            name='website_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Website URL'),
        ),
        migrations.AlterField(
            model_name='userphoto',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Photo'),
        ),
        migrations.AlterField(
            model_name='userphoto',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
