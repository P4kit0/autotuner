# Generated by Django 4.2.5 on 2023-10-07 08:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+905551234567'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('credit_amount', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DtcInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ecu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='EcuBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EngineVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FileProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FileRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_price', models.IntegerField()),
                ('file_type', models.CharField(choices=[('E', 'ECU file'), ('T', 'Transmission File')], max_length=1)),
                ('transmissin', models.CharField(choices=[('A', 'AUTO'), ('M', 'MANUAL')], max_length=1)),
                ('tool_type', models.CharField(choices=[('S', 'Slave'), ('M', 'Master')], max_length=1)),
                ('original_file', models.FileField(upload_to='uploads/original/')),
                ('processed_file', models.FileField(null=True, upload_to='uploads/processed/')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='database.customer')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.employee')),
                ('processes', models.ManyToManyField(to='database.fileprocess')),
                ('tool', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tool', to='database.connectiontool')),
            ],
        ),
        migrations.CreateModel(
            name='FileSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/for_sale/')),
                ('desc', models.TextField(max_length=400)),
                ('price', models.IntegerField()),
                ('owners', models.ManyToManyField(to='database.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='database.vehiclebrand')),
                ('versions', models.ManyToManyField(to='database.engineversion')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp', models.IntegerField()),
                ('year', models.IntegerField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='database.vehiclecategory')),
                ('ecu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ecu', to='database.ecu')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model', to='database.vehiclemodel')),
                ('version', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='version', to='database.engineversion')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('E', 'Expense'), ('D', 'Deposit')], max_length=1)),
                ('amount', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.customer')),
                ('file_bought', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.filesale')),
                ('file_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.filerequest')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.fileprocess')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='KnowledgePart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('knowledge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.knowledge')),
            ],
        ),
        migrations.CreateModel(
            name='KnowledgeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=400)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.knowledgepart')),
            ],
        ),
        migrations.AddField(
            model_name='filesale',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.vehicle'),
        ),
        migrations.AddField(
            model_name='filerequest',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.vehicle'),
        ),
        migrations.CreateModel(
            name='EcuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.ecubrand')),
            ],
        ),
        migrations.AddField(
            model_name='ecu',
            name='car_brands',
            field=models.ManyToManyField(to='database.vehiclebrand'),
        ),
        migrations.AddField(
            model_name='ecu',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.ecumodel'),
        ),
    ]
