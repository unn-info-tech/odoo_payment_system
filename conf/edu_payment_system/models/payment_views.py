from odoo import models, fields

class EduPaymentStudents(models.Model):
    _name = 'edu.payment'
    _description = 'Payment of Students'

    student_id = fields.Many2one('edu.student', string='Student', required=True)
    amount = fields.Float(string='Amount', required=True)
    payment_date = fields.Date(string='Payment Date', required=True)
    description = fields.Text(string='Description')
