# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_stage(models.Model):
    _name = 'help_desk.stage'

    name = fields.Char(string="Name", required=True)
    main_template_ids = fields.Many2many('mail.template', string="Mail Template")
    is_cancel_button_visible = fields.Boolean(string="Is Cancel Button Visible ?")
    is_done_button_visible = fields.Boolean(string="Is Resolved Button Visible ?")
    sh_next_stage = fields.Many2one('help_desk.stage', string="Next Stage")
    sh_group_ids = fields.Many2many('res.groups', string="Groups")
