# -*- coding: utf-8 -*-

from odoo import models, fields, api, _



class HosAppointment(models.Model):
    _name = 'hos.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Appointment'
    _rec_name = 'patient_id'

    def _get_default_note(self):
        return "Subscribe our YouTube channel"

    patient_id = fields.Many2one('hos.patient', string='Patient', required=True, default= lambda self: self.env.user)
    patient_age = fields.Integer(string='Age', related='patient_id.patient_age')
    notes = fields.Text(string="Registration Note", default=_get_default_note)
    appointment_date = fields.Date(string='Date', required=True)



