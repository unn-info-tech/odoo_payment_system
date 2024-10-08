from odoo import models, fields

class EduTeacher(models.Model):
    _name = 'edu.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Teacher Name', required=True)
    # Define a Many2many relationship with the group model once it's created
    #group_ids = fields.Many2many('edu.group', string='Groups')
