# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_teams(models.Model):
    _name = 'help_desk.team'

    name = fields.Char(string="Name")
    working_schedule = models.Many2one('resource.calendar', string="Working Schedule")
    team_head = models.Many2one('res.users', string="Team Head")
    team_members = models.Many2many('res.users', string="Team Members")