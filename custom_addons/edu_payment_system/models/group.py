from odoo import models, fields
from odoo import models, fields, api

class EduGroup(models.Model):
    _name = 'edu.group'
    _description = 'Group'

    name = fields.Char(string='Group Name', required=True)
    description = fields.Text(string='Description')
    teacher_ids = fields.Many2many('edu.teacher', string='Teachers')  
    student_ids = fields.Many2many('edu.student', string='Students')  
    course_ids = fields.Many2many('edu.course', string='Courses')
    payment_ids = fields.One2many('edu.payment', compute='_compute_payments', string='Payments')

    @api.depends('student_ids')
    def _compute_payments(self):
        for group in self:
            student_ids = group.student_ids.ids
            payments = self.env['edu.payment'].search([('student_id', 'in', student_ids)])
            group.payment_ids = payments
    
