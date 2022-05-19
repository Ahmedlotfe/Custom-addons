# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_alarm(models.Model):
    _name = 'help_desk.alarm'

    name = fields.Char(string="Name", default="0 Hour(s) [email]", compute="_get_name", readonly=True)
    sh_reminder_before = fields.Integer(string="Reminder Before", default=0)
    sh_reminder_unit = fields.Selection([
        ('Hour(s)', 'Hour(s)'),
        ('Minute(s)', 'Minute(s)'),
        ('Second(s)', 'Second(s)'),
    ], string="Reminder Unit", default='Hour(s)', required=True)

    type = fields.Selection([
        ('email', 'Email'),
        ('popup', 'Popup'),
    ], string="Type", required=True)

    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)

    @api.depends('sh_reminder_before', 'sh_reminder_unit')
    def _get_name(self):
        for rec in self:
            if rec.sh_reminder_before and rec.sh_reminder_unit:
                rec.name = f"{rec.sh_reminder_before} {rec.sh_reminder_unit}[email]"
