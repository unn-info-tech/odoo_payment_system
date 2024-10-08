from odoo import models, fields

class EduSalaryPayment(models.Model):
    _name = 'edu.salary'
    _description = 'Salary Payment Management'

    teacher_id = fields.Many2one('edu.teacher', string='Teacher', required=True)
    amount = fields.Float(string='Amount', required=True)
    payment_date = fields.Date(string='Payment Date', required=True)
    description = fields.Text(string='Description')
