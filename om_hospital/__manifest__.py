# -*- coding: utf/8 -*-

{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Ahmed Lotfe',
    'sequence': -100,
    'summary': 'Hospital management system',
    'description': """Hospital management system description""",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tags.xml',
    ],
    'demo': [
        'data/patient_tag_data.xml'
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}