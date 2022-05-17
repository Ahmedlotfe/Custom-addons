# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_alarm(models.Model):
    _name = 'help_desk.alarm'

    name = fields.Char(string="Name", readonly=True)
    sh_reminder_before = fields.Integer(string="Reminder Before")
    sh_reminder_unit = fields.Selection([
        ('Hour(s)', 'Hour(s)'),
        ('Minute(s)', 'Minute(s)'),
        ('Second(s)', 'Second(s)'),
    ], string="Reminder Unit", required=True)

    type = fields.Selection([
        ('email', 'Email'),
        ('popup', 'Popup'),
    ], string="Type", required=True)

    company_id = fields.Many2one('res.company', string="Company")


