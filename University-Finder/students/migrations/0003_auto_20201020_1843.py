# Generated by Django 3.1.1 on 2020-10-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_courses_suggestion_topics_univdegree_university'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestion',
            name='topic4',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='topic5',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
