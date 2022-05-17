# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_priorities(models.Model):
    _name = 'help_desk.priorities'

    name = fields.Char(string="Name", required=True)

