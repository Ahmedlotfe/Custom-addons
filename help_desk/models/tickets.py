# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_ticket(models.Model):
    _name = 'help_desk.ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    email_subject = fields.Char()
    company_id = fields.Many2one('res.company', readonly=True, default=lambda self: self.env.company)
    state = fields.Selection([
        ('customer_replied', 'Customer Replied'),
        ('staff_replied', 'Staff Replied')
    ], required=True, string="Replied Status")

    ticket_type = fields.Many2one('help_desk.ticket.type', string="Ticket Type")
    team_id = fields.Many2one('help_desk.team', string="Team")
    team_head = fields.Many2one('res.users', string="Team Head", compute="_get_team_head", readonly=True)
    user_id = fields.Many2one('res.users', string="Assigned User")
    subject_id = fields.Many2one('help_desk.subject.type', string="Ticket Subject Type")
    tags_ids = fields.Many2many('help_desk.tag', string="Tags")
    priority = fields.Many2one('help_desk.priorities', string="Priority")
    duration = fields.Float(string="Real Duration", readonly=True)
    create_date = fields.Datetime(string="Create Date", default=fields.Datetime.now, readonly=True)
    write_date = fields.Datetime(string="Last Update Date")
    sh_due_date = fields.Datetime(string="Reminder Due Date", default=fields.Datetime.now)
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    person_name = fields.Char(string="Person Name")
    email = fields.Char(string="Email")
    mobile_no = fields.Char(string="Mobile")
    replied_date = fields.Datetime(string="Replied Date")
    sh_ticket_alarm_ids = fields.Many2many('help_desk.alarm', string="Ticket Reminders")
    description = fields.Html(string="Description")
    attachment_ids = fields.Many2many('ir.attachment')
    timesheet_ids = fields.Many2many('account.analytic.line')
    close_date = fields.Datetime(string="Close Date")
    close_by = fields.Many2one('res.users', string="Closed By")
    comment = fields.Text(string="Closed Comment")
    cancel_date = fields.Datetime(string="Cancelled Date")
    cancelled_by = fields.Many2one('res.users', string="Cancelled By")
    cancel_reason = fields.Char(string="Cancel Reason")
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('closed', 'Closed'),
        ('cancel', 'Cancel'),
        ('reopened', 'Reopened')], default='new', string="Status", required=True)

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.person_name = self.partner_id.name
        self.email = self.partner_id.email



    @api.depends('team_id')
    def _get_team_head(self):
        for rec in self:
            if rec.team_id:
                rec.team_head = rec.team_id.team_head
            else:
                rec.team_head = ""


    def action_test(self):
        print("Hello! World")