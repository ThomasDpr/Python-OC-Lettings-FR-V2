"""
Data migration to copy lettings data from oc_lettings_site to lettings app.

This migration copies existing Address and Letting records from the
original oc_lettings_site application to the new lettings application
as part of the modular architecture refactoring.
"""

from django.db import migrations


def copy_lettings_data(apps, schema_editor):
    """
    Copy Address and Letting data from oc_lettings_site to lettings app.

    Iterates through all existing Address and Letting records in the
    oc_lettings_site app and creates corresponding records in the
    lettings app, preserving original IDs and relationships.

    Args:
        apps: Django apps registry for accessing historical models.
        schema_editor: Database schema editor instance.
    """
    OldAddress = apps.get_model("oc_lettings_site", "Address")
    OldLetting = apps.get_model("oc_lettings_site", "Letting")

    NewAddress = apps.get_model("lettings", "Address")
    NewLetting = apps.get_model("lettings", "Letting")

    for addr in OldAddress.objects.all():
        NewAddress.objects.create(
            id=addr.id,
            number=addr.number,
            street=addr.street,
            city=addr.city,
            state=addr.state,
            zip_code=addr.zip_code,
            country_iso_code=addr.country_iso_code,
        )

    for letting in OldLetting.objects.all():
        NewLetting.objects.create(
            id=letting.id,
            title=letting.title,
            address_id=letting.address_id,
        )


def reverse_copy_lettings_data(apps, schema_editor):
    """
    Reverse the data migration by deleting copied records.

    Removes all Letting and Address records from the lettings app
    to revert to the previous state.

    Args:
        apps: Django apps registry for accessing historical models.
        schema_editor: Database schema editor instance.
    """
    apps.get_model("lettings", "Letting").objects.all().delete()
    apps.get_model("lettings", "Address").objects.all().delete()


class Migration(migrations.Migration):
    """
    Data migration for copying lettings data between applications.

    This migration depends on both the lettings initial migration and
    the oc_lettings_site initial migration to ensure both source and
    target models exist.
    """

    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_lettings_data, reverse_copy_lettings_data),
    ]
