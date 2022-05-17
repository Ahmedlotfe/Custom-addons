# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class attendance(models.Model):
    _name = 'attendance.attendee'
    _description = 'attendance.attendance'

    name = fields.Many2one('hr.employee', string="Name")
    register_date = fields.Datetime(string="Register date", required=True)
    last_date = fields.Datetime(string="Last date", required=True)
    total_time = fields.Char(string="Total Time", compute="_get_total_time", readonly=True)

    @api.depends('register_date', 'last_date')
    def _get_total_time(self):
        for rec in self:
            if rec.register_date and rec.last_date:
                start_date = rec.register_date
                end_date = rec.last_date
                total = relativedelta(end_date, start_date)
                rec.total_time = str(total.months) + "Month" + "   "  + str(total.days) + "Day" + "   " + str(total.hours) + "Hour" + "   " + str(total.minutes) + "Minute"

            else:
                rec.total_time = ""