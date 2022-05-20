# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class HosPatient(models.Model):
    _name = 'hos.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'

    name = fields.Char(string="Name")
    patient_age = fields.Integer(string="Age", tracking=True)
    notes = fields.Text(string="Notes")
    image = fields.Binary(string="Image")
    name_seq = fields.Char(string="Order Reference", required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender")
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], string="Age Group", compute="_get_group", readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hos.patient.sequence') or _('New')
        result = super(HosPatient, self).create(vals)
        return result

    @api.depends('patient_age')
    def _get_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age > 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'
            else:
                rec.age_group = ''


    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5:
                raise ValidationError("The age must be greater than 5")