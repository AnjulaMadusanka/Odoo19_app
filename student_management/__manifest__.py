# -*- coding: utf-8 -*-

{
    'name': 'Student Management',           # Display name in Apps
    'version': '1.0',                        # Module version
    'category': 'Custom',                 # Category in Apps menu
    'summary': 'Simple student records',     # Short description
    'description': """
        Student Management Module
        =========================
        A simple module to manage student information:
        - Student name, email, phone
        - Date of birth and enrollment date
        - Course/class and notes
    """,
    'author': 'Anjula Wijekoon',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['base'],                     # We only need Odoo base (no other modules)
    'data': [
        'security/ir.model.access.csv',      # Who can read/write student data
        'views/student_views.xml',           # List and form views + menu
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
