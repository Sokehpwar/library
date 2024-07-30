# -*- coding: utf-8 -*-
{
    "name": "Library Book Extension",
    "version": "17.0.0.1",
    "depends": [
        "base"
    ],
    "external_dependencies": {},
    "author": "NNEK",
    "website": "https://sokehpwarlay.blogspot.com/, https://apps.odoo.com/apps/modules/17.0/custom_payment_sequence",
    "summary": """Library Book Extension""",
    "description": """
        Library Extension
    """,
    "category": "Extra Tools",
    "data": [
        "security/ir.model.access.csv",
        "views/library_book_view.xml",
        "views/library_book_category_views.xml",
        "views/library_menus.xml",
    ],
    'images': ['static/description/icon.png'],
    "installable": True,
    "application": False,
}
