# Generated by Django 3.1 on 2021-01-25 14:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('layout_image', '0013_auto_20201223_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layout',
            name='layout_id',
            field=models.UUIDField(default=uuid.UUID('b42777df-02fc-4a7e-a8c6-dc9d5d847a20'), editable=False, primary_key=True, serialize=False, verbose_name='编排UUID'),
        ),
        migrations.AlterField(
            model_name='layoutdata',
            name='layout_user_id',
            field=models.UUIDField(default=uuid.UUID('56487b3b-0cdd-402a-b9a5-c81453a0ef71'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservice',
            name='service_id',
            field=models.UUIDField(default=uuid.UUID('4d98667f-3313-4c1a-b233-08f697cdeffe'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicecontainer',
            name='service_container_id',
            field=models.UUIDField(default=uuid.UUID('96c081f8-d897-4c3e-8947-bd96d04c07e1'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicecontainerscore',
            name='layout_service_container_score_id',
            field=models.UUIDField(default=uuid.UUID('3e0c0c55-09ce-4cff-b303-312b62d7b70b'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='layoutservicenetwork',
            name='layout_service_network_id',
            field=models.UUIDField(default=uuid.UUID('a5d28af1-2dd2-485c-8ebf-f457dc155b02'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
