# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_project(models.Model):
    _inherit = 'project.project'

    allow_timesheets = fields.Boolean(string="Timesheets", default=True)
    allow_billable = fields.Boolean(string="Billable", default=False)
    allow_recurring_tasks = fields.Boolean(string="Recurring Tasks", default=True)
    alias_name = fields.Char(string="Create tasks by sending an email to",
                             help="The name of email alias, e.g 'jobs' if you want to catch email for <jobs@example.odoo.com>")
