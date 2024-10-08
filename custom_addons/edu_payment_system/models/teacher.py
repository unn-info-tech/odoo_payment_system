from odoo import models, fields

class EduTeacher(models.Model):
    _name = 'edu.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Teacher Name', required=True)
    about = fields.Text(string='About')
    email = fields.Char(string='Email')



    
