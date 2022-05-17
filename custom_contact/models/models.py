# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_contact(models.Model):
    _inherit = 'res.partner'

    company_staff = fields.Many2many('client_staff.client_employee', string="Company Staff")

