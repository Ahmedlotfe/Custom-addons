# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Custom_Department(models.Model):
    _inherit = 'hr.department'

    company_id = fields.Many2one('res.company', string="Company")