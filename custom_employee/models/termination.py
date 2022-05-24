# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee_Termination(models.Model):
    _name = 'employee.termination'

    name = fields.Many2one('hr.employee', string="Name", required=True)
    job_title = fields.Char(string="Job Title")
    termination_reason = fields.Selection([
        ('1', 'انتهاء عقد العمل'),
        ('2', 'انقطاع عن العمل'),
        ('3', 'افشاء اسرار المؤسسه'),
        ('4', 'التقاعد'),
        ('5', 'الوفاه'),
        ('6', 'الاستقاله'),
        ('7', 'انتهاء فترة التدريب'),
        ('8', 'سبب اخر'),
    ], string="Termination Reason")
    date = fields.Date(string="Date", required=True)
    name_id = fields.Many2one('employee.custody', string='Name')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('delivered', 'Delivered'),
        ('returned', 'Returned')
    ], string='State', related="name_id.state", readonly=True)