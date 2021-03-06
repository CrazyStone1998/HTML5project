# Generated by Django 2.0.7 on 2018-11-26 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weCheck', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave',
            fields=[
                ('leaveID', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=0)),
                ('result', models.CharField(max_length=100)),
                ('reMsg', models.CharField(max_length=100)),
                ('checkID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weCheck.check')),
                ('groupID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weCheck.group')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weCheck.user')),
            ],
        ),
    ]
