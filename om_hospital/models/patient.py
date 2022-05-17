from datetime import date
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference')
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True, default='male')
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.One2many('hospital.appointment', 'patient_id', string="Appointment")


    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0



class HospitalPatientTags(models.Model):
    _name = "patient.tags"

    name = fields.Char(string="Name")
    active = fields.Boolean(string="Active", default=True)