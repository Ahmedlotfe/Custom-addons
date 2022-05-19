# -*- coding: utf-8 -*-
{
    'name': "help_desk",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "mail", "portal","mail"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/help_desk_ticket_type.xml',
        'views/help_desk_subject_type.xml',
        'views/help_desk_tag.xml',
        'views/help_desk_stage.xml',
        'views/help_desk_category.xml',
        'views/help_desk_sub_category.xml',
        'views/help_desk_priorities.xml',
        'views/help_desk_sla_policies.xml',
        'views/help_desk_alarm.xml',
        'views/help_desk_ticket.xml',
        'views/help_desk_send_quickly_reply.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
