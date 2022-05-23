# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ProjectTask(models.Model):
    _inherit = 'project.task'

    user_id = fields.Many2one('res.users', string="Assigned to")
    start_time = fields.Datetime(readonly=True)
    end_time = fields.Datetime(readonly=True)
    duration = fields.Char(compute="_get_duration", store=True, readonly=True, string="Real Duration")

    sequence = fields.Integer(string="Sequence")
    email_cc = fields.Char(string="Email cc")
    company_id = fields.Many2one('res.company', string="Company")
    allow_user_ids = fields.Many2many('res.users', string="Visible to")
    project_privacy_visibility = fields.Selection([
        ('followers', 'Invited internal users'),
        ('employees', 'All internal users'),
        ('portal', 'Invited portal users and all internal users')
    ], string="Project Visibility")
    analytic_account_id = fields.Many2one('account.analytic.account', string="Analytic Account", readonly=True)

    displayed_image_id = fields.Many2one('ir.attachment', string="Cover Image")
    date_assign = fields.Datetime(default=fields.Datetime.now, string="Assigning Date", readonly=True)
    date_last_stage_update = fields.Datetime(default=fields.Datetime.now, string="Last Stage Update", readonly=True)

    def get_start_date(self):
        for rec in self:
            rec.start_time = datetime.now()

    def get_end_date(self):
        for rec in self:
            rec.end_time = datetime.now()

    @api.depends('start_time', 'end_time')
    def _get_duration(self):
        for rec in self:
            if rec.start_time and rec.end_time:
                sd = rec.start_time
                ed = rec.end_time
                rd = relativedelta(ed, sd)
                rec.duration = str(rd.months) + "Month" + "   " + str(rd.days) + "Day" + "   " + str(
                    rd.hours) + "Hour" + "   " + str(rd.minutes) + "Minute"
            else:
                rec.duration = "Start Time and | or  End Time Not Set"
