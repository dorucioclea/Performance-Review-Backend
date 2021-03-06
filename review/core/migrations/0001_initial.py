# Generated by Django 3.0 on 2019-12-08 13:15

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=512)),
                ('rating', models.IntegerField(choices=[(1, 'NEEDS_IMPROVMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'STRONGLY_EXCEEDS_EXPECTATIONS'), (5, 'SUPERB')])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Project')),
                ('reviewee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=512)),
                ('rating', models.IntegerField(choices=[(1, 'NEEDS_IMPROVMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'STRONGLY_EXCEEDS_EXPECTATIONS'), (5, 'SUPERB')])),
                ('project_review', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.ProjectReview')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sahabiness_rating', models.IntegerField(choices=[(1, 'NEEDS_IMPROVMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'STRONGLY_EXCEEDS_EXPECTATIONS'), (5, 'SUPERB')])),
                ('sahabiness_comment', models.CharField(max_length=280)),
                ('problem_solving_rating', models.IntegerField(choices=[(1, 'NEEDS_IMPROVMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'STRONGLY_EXCEEDS_EXPECTATIONS'), (5, 'SUPERB')])),
                ('problem_solving_comment', models.CharField(max_length=280)),
                ('execution_rating', models.IntegerField(choices=[(1, 'NEEDS_IMPROVMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'STRONGLY_EXCEEDS_EXPECTATIONS'), (5, 'SUPERB')])),
                ('execution_comment', models.CharField(max_length=280)),
                ('thought_leadership_rating', models.IntegerField(choices=[(1, 'NEEDS_IMPROVMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'STRONGLY_EXCEEDS_EXPECTATIONS'), (5, 'SUPERB')])),
                ('thought_leadership_comment', models.CharField(max_length=280)),
                ('leadership_rating', models.IntegerField(choices=[(1, 'NEEDS_IMPROVMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'STRONGLY_EXCEEDS_EXPECTATIONS'), (5, 'SUPERB')])),
                ('leadership_comment', models.CharField(max_length=280)),
                ('presence_rating', models.IntegerField(choices=[(1, 'NEEDS_IMPROVMENT'), (2, 'MEETS_EXPECTATIONS'), (3, 'EXCEEDS_EXPECTATIONS'), (4, 'STRONGLY_EXCEEDS_EXPECTATIONS'), (5, 'SUPERB')])),
                ('presence_comment', models.CharField(max_length=280)),
                ('strengths', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=280), size=3)),
                ('weaknesses', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=280), size=3)),
                ('reviewee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='authored_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
