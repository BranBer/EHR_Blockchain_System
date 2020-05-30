# Generated by Django 3.0.4 on 2020-05-22 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EHR_System', '0010_auto_20200522_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phys_exam',
            name='heart',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='phys_exam', to='EHR_System.Phys_Exam_Heart'),
        ),
        migrations.AlterField(
            model_name='phys_exam',
            name='vitals',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='phys_exam', to='EHR_System.Phys_Exam_Vitals'),
        ),
    ]