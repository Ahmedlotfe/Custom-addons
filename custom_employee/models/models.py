# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee_Custody(models.Model):
    _name = 'employee.custody'
    _rec_name = 'name_id'

    name_id = fields.Many2one('hr.employee', string="Name", required=True)
    type = fields.Selection([
        ('item', 'Item'),
        ('money', 'Money'),
    ], required=True)
    item_name = fields.Char(string="Item Name")
    serial_number = fields.Char(string="Serial Number")
    date = fields.Date(string="Date", required=True)
    amount = fields.Integer('Amount', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('delivered', 'Delivered'),
        ('returned', 'Returned')
    ], string='State', default='draft')

    def get_draft(self):
        self.state = 'draft'

    def get_delivered(self):
        self.state = 'delivered'

    def get_returned(self):
        self.state = 'returned'
