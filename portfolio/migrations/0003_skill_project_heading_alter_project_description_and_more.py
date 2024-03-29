# Generated by Django 4.0.1 on 2022-08-28 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(unique=True)),
                ('heading', models.BooleanField(default=True)),
                ('skill_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='heading',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='ProjectResponsebility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(unique=True)),
                ('heading', models.BooleanField(default=True)),
                ('response', models.TextField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsebility', to='portfolio.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(unique=True)),
                ('heading', models.BooleanField(default=True)),
                ('image', models.CharField(max_length=1000)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(to='portfolio.Skill'),
        ),
    ]
