# -*- coding: utf-8 -*-

from odoo import models, fields, api


class client_staff(models.Model):
    _name = 'client_staff.client_employee'

    name = fields.Char(string="Name")
    title = fields.Selection([
        ('mr', 'Mr.'),
        ('mrs', 'Mrs.'),
        ('ms', 'Ms.'),
        ('fr', 'Fr.'),
        ('sr', 'Sr.'),
        ('rev', 'Rev.'),
        ('dr', 'Dr.'),
        ('other', 'Other'),
    ], default='mr')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'female'),
    ])
    address = fields.Char(string="Address")
    job_title = fields.Char(string="Job Title")
    email = fields.Char(string="Email")
    comapny_name = fields.Many2one('res.partner')
    phone_number = fields.Char("Phone Number")
    notes = fields.Text(string="Notes")


