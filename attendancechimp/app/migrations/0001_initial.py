# Generated by Django 4.2 on 2024-04-08 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "auto_increment_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=128)),
                ("class_start", models.TimeField()),
                ("class_end", models.TimeField()),
                ("m_class", models.BooleanField(default=False)),
                ("tu_class", models.BooleanField(default=False)),
                ("w_class", models.BooleanField(default=False)),
                ("th_class", models.BooleanField(default=False)),
                ("f_class", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="UniversityPerson",
            fields=[
                (
                    "auto_increment_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("is_instructor", models.BooleanField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QRCodeUpload",
            fields=[
                (
                    "auto_increment_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("image", models.ImageField(upload_to="data")),
                ("uploaded", models.DateTimeField(auto_now_add=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.course"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.universityperson",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QRCode",
            fields=[
                (
                    "auto_increment_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("code", models.CharField(max_length=32)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.course"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="instructor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.universityperson"
            ),
        ),
    ]
