# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ProjectTask(models.Model):
    _inherit = 'project.task'

    user_id = fields.Many2one('res.users', string="Assigned to")
    # duration = fields.Char(compute="_get_duration", store=True, readonly=True)

    company_id = fields.Many2one('res.company', string="Company")
    allow_user_ids = fields.Many2many('res.users', string="Visible to")
    project_privacy_visibility = fields.Selection([
        ('followers', 'Invited internal users'),
        ('employees', 'All internal users'),
        ('portal', 'Invited portal users and all internal users')
    ], string="Project Visibility")
    analytic_account_id = fields.Many2one('account.analytic.account', string="Analytic Account", readonly=True)

    planned_hours = fields.Float(string="Initially Planned Hours")
    progress = fields.Float(string="Progress")
    timesheet_ids = fields.Many2many('account.analytic.line')

    #
    # def get_start_date(self):
    #     for rec in self:
    #         rec.start_time = datetime.now()
    #
    # def get_end_date(self):
    #     for rec in self:
    #         rec.end_time = datetime.now()
    #
    # @api.depends('start_time', 'end_time')
    # def _get_duraation(self):
    #     for rec in self:
    #         if rec.start_time and rec.end_time:
    #             sd = rec.start_time
    #             ed = rec.end_time
    #             rd = relativedelta(ed, sd)
    #             rec.duration = str(rd.months) + "Month" + "   " + str(rd.days) + "Day" + "   " + str(
    #                 rd.hours) + "Hour" + "   " + str(rd.minutes) + "Minute"
    #         else:
    #             rec.duration = "Start Time and | or  End Time Not Set"
