# Generated by Django 3.2.4 on 2021-06-08 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('enabled', models.BooleanField(default=False)),
                ('owner', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_tenant', models.CharField(max_length=32, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favorite', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default='')),
                ('orphan', models.BooleanField(default=False)),
                ('state', models.CharField(max_length=64)),
                ('service_offering_ref', models.CharField(max_length=64)),
                ('service_offering_source_ref', models.CharField(blank=True, default='', max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('long_description', models.TextField(blank=True, default='')),
                ('distributor', models.CharField(max_length=64)),
                ('documentation_url', models.URLField(blank=True)),
                ('support_url', models.URLField(blank=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.portfolio')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tenant')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='portfolio',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.tenant'),
        ),
        migrations.AddConstraint(
            model_name='portfolioitem',
            constraint=models.CheckConstraint(check=models.Q(('name__length__gt', 0)), name='catalog_portfolioitem_name_empty'),
        ),
        migrations.AddConstraint(
            model_name='portfolioitem',
            constraint=models.CheckConstraint(check=models.Q(('service_offering_ref__length__gt', 0)), name='catalog_portfolioitem_service_offering_empty'),
        ),
        migrations.AddConstraint(
            model_name='portfolioitem',
            constraint=models.UniqueConstraint(fields=('name', 'tenant', 'portfolio'), name='catalog_portfolioitem_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='portfolio',
            constraint=models.CheckConstraint(check=models.Q(('name__length__gt', 0)), name='catalog_portfolio_name_empty'),
        ),
        migrations.AddConstraint(
            model_name='portfolio',
            constraint=models.UniqueConstraint(fields=('name', 'tenant'), name='catalog_portfolio_name_unique'),
        ),
    ]