# Generated by Django 4.1 on 2022-09-12 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_article_scope_scopes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='scopes',
            new_name='article',
        ),
    ]