from odoo import models, fields
from odoo import models, fields, api

class Student(models.Model):
    _name = 'edu.student'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True)
    about = fields.Text(string='About')
    email = fields.Char(string='Email')
    payment_ids = fields.One2many('edu.payment', "student_id", string='Payments')


    
