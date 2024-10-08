from odoo import models, fields, api
from datetime import datetime, timedelta

class EduPaymentStudents(models.Model):
    _name = 'edu.payment'
    _description = 'Payment of Students'

    student_id = fields.Many2one('edu.student', string='Student', required=True, ondelete='cascade')
    amount = fields.Float(string='Amount', required=True)
    payment_date = fields.Date(string='Payment Date', required=True)
    description = fields.Text(string='Description')
    
    
   

  