# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_sla_policies(models.Model):
    _name = 'help_desk.sla_policies'

    name = fields.Char(required=True)
    sh_team_id = fields.Many2one('help_desk.team', string="Helpdesk Team", required=True)
    company_id = fields.Many2one('res.company', string="Company")
    sh_ticket_type_id = fields.Many2one('help_desk.ticket.type', string="Helpdesk Team Type")
    sh_sla_target_type = fields.Selection([
        ('reaching_stage', 'Reaching Stage'),
        ('assigned_to', 'Assigned To')
    ], string="SLA Target Type")
    sh_stage_id = fields.Many2one('help_desk.stage', string="Reach Stage")
    sh_ticket_type_id = fields.Many2one('help_desk.ticket.type', string="Helpdesk Team Type")
    sh_days = fields.Integer(string="Reach In", required=True)



