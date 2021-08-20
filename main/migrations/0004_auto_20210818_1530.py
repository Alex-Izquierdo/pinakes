# Generated by Django 3.2.5 on 2021-08-18 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210805_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('level', models.CharField(choices=[('Info', 'Info'), ('Error', 'Error'), ('Warning', 'Warning'), ('Debug', 'Debug')], default='Info', editable=False, max_length=10)),
                ('received_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True, default='')),
                ('messageable_type', models.CharField(max_length=64, null=True)),
                ('messageable_id', models.IntegerField(editable=False, null=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='ApprovalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approval_request_ref', models.CharField(default='', max_length=64)),
                ('reason', models.TextField(blank=True, default='')),
                ('request_completed_at', models.DateTimeField(editable=False, null=True)),
                ('state', models.CharField(choices=[('Undecided', 'Undecided'), ('Approved', 'Approved'), ('Canceled', 'Canceled'), ('Denied', 'Denied'), ('Failed', 'Failed')], default='Undecided', editable=False, max_length=10)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.order')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tenant')),
            ],
        ),
        migrations.AddIndex(
            model_name='progressmessage',
            index=models.Index(fields=['tenant', 'messageable_id', 'messageable_type'], name='main_progre_tenant__e6daa2_idx'),
        ),
        migrations.AddIndex(
            model_name='approvalrequest',
            index=models.Index(fields=['tenant', 'order'], name='main_approv_tenant__9d790f_idx'),
        ),
    ]