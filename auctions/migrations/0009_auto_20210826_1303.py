# Generated by Django 3.2.5 on 2021-08-26 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_rename_user_id_listings_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='auction',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auctions.listings'),
        ),
        migrations.AddField(
            model_name='bids',
            name='bid_price',
            field=models.IntegerField(default='1000'),
        ),
        migrations.AddField(
            model_name='bids',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(default='abc', max_length=150)),
                ('auction', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auctions.listings')),
                ('user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
