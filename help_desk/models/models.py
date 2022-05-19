# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_teams(models.Model):
    _name = 'help_desk.team'

    name = fields.Char(string="Name")
    working_schedule = fields.Many2one('resource.calendar', string="Working Schedule")
    team_head = fields.Many2one('res.users', string="Team Head")
    team_members = fields.Many2many('res.users', string="Team Members")
