# Generated by Django 4.1.7 on 2023-03-16 08:34

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("main", "0003_post_modifieddate_post_publisheddate"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tag",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
