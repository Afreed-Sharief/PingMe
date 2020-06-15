# Generated by Django 3.0.6 on 2020-06-14 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pingme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followuser',
            name='followed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to='Pingme.MyProfile'),
        ),
        migrations.AlterField(
            model_name='followuser',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='Pingme.MyProfile'),
        ),
        migrations.AlterField(
            model_name='mypost',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pingme.MyProfile'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='commented_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pingme.MyProfile'),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='liked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pingme.MyProfile'),
        ),
    ]
