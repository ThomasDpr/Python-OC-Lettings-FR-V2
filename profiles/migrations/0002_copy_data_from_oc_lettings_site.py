"""
Data migration to copy profiles data from oc_lettings_site to profiles app.

This migration copies existing Profile records from the original
oc_lettings_site application to the new profiles application
as part of the modular architecture refactoring.
"""

from django.db import migrations


def copy_profiles_data(apps, schema_editor):
    """
    Copy Profile data from oc_lettings_site to profiles app.

    Iterates through all existing Profile records in the oc_lettings_site
    app and creates corresponding records in the profiles app,
    preserving original IDs and user relationships.

    Args:
        apps: Django apps registry for accessing historical models.
        schema_editor: Database schema editor instance.
    """
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    NewProfile = apps.get_model("profiles", "Profile")

    for profile in OldProfile.objects.all():
        NewProfile.objects.create(
            id=profile.id,
            user_id=profile.user_id,
            favorite_city=profile.favorite_city,
        )


def reverse_copy_profiles_data(apps, schema_editor):
    """
    Reverse the data migration by deleting copied records.

    Removes all Profile records from the profiles app
    to revert to the previous state.

    Args:
        apps: Django apps registry for accessing historical models.
        schema_editor: Database schema editor instance.
    """
    apps.get_model("profiles", "Profile").objects.all().delete()


class Migration(migrations.Migration):
    """
    Data migration for copying profiles data between applications.

    This migration depends on both the profiles initial migration and
    the oc_lettings_site initial migration to ensure both source and
    target models exist.
    """

    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_profiles_data, reverse_copy_profiles_data),
    ]
