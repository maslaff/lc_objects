# Generated by Django 5.0.1 on 2024-02-20 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects_db', '0005_rename_id_system_controlpanels_system'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cctvcameras',
            old_name='id_cctv_system_manufacturer',
            new_name='cctv_system_manufacturer',
        ),
        migrations.RenameField(
            model_name='cctvcameras',
            old_name='id_cctv_system_type',
            new_name='cctv_system_type',
        ),
        migrations.RenameField(
            model_name='cctvcameras',
            old_name='id_videorecorder',
            new_name='videorecorder',
        ),
        migrations.RenameField(
            model_name='cctvrecorders',
            old_name='id_cctv_system_manufacturer',
            new_name='cctv_system_manufacturer',
        ),
        migrations.RenameField(
            model_name='cctvrecorders',
            old_name='id_cctv_system_type',
            new_name='cctv_system_type',
        ),
        migrations.RenameField(
            model_name='cctvrecorders',
            old_name='id_system',
            new_name='system',
        ),
        migrations.RenameField(
            model_name='networkdevices',
            old_name='id_network_device_model',
            new_name='network_device_model',
        ),
        migrations.RenameField(
            model_name='networkdevices',
            old_name='id_system',
            new_name='system',
        ),
    ]
