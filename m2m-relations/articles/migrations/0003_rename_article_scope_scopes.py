# Generated by Django 4.1 on 2022-09-08 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_alter_article_options_tag_scope_article_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='article',
            new_name='scopes',
        ),
    ]
