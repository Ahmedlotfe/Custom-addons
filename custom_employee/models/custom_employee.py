# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta


class Employee_Custody(models.Model):
    _inherit = 'hr.employee'

    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    upload_cv = fields.Binary(string="Upload Cv")
    custody_check = fields.Integer(string="Custody Count", compute="_custody_count", readonly=True)
    custody_ids = fields.One2many('employee.custody', 'name_id')
    leave_manager_id = fields.Many2one('res.users', string="Time Off")

    @api.depends('name', 'custody_ids')
    def _custody_count(self):
        for rec in self:
            if rec.name:
                rec.custody_check = len(rec.custody_ids)
            else:
                rec.custody_check = 0

    age_total = fields.Char(string="Age Total", compute="_get_total_age", readonly=True)

    @api.depends('birthday')
    def _get_total_age(self):
        today = date.today()
        for rec in self:
            if rec.birthday:
                total = relativedelta(today, rec.birthday)
                rec.age_total = str(total.years) + "Year" + "   " + str(total.months) + "Month" + "   " + str(
                    total.days) + "Day"
            else:
                rec.age_total = "No Date Of Birth!!"

    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    timesheet_cost = fields.Monetary(string='Timesheet Cost')
