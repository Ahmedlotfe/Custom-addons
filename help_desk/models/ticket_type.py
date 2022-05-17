# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_ticket_type(models.Model):
    _name = 'help_desk.ticket.type'

    name = fields.Char(string="Name")
