from odoo import models, fields

class EduCourse(models.Model):
    _name = 'edu.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
