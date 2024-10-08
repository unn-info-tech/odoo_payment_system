from odoo import models, fields

class Student(models.Model):
    _name = 'edu.student'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    email = fields.Char(string='Email')
