# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_subject_type(models.Model):
    _name = 'help_desk.subject.type'

    name = fields.Char(string="Name")
