# -*- coding: utf-8 -*-

from odoo import models, fields, api


class send_quick_reply(models.Model):
    _name = 'help_desk.send_quick_reply'

    title = fields.Char(string="Title", required=True)
    user = fields.Many2one('res.users', string="User")
    common_for_all = fields.Boolean(string="Common For All")
    body = fields.Html(string="Body")
