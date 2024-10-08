# -*- coding: utf-8 -*-
# from odoo import http


# class EduPaymentSystem(http.Controller):
#     @http.route('/edu_payment_system/edu_payment_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edu_payment_system/edu_payment_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('edu_payment_system.listing', {
#             'root': '/edu_payment_system/edu_payment_system',
#             'objects': http.request.env['edu_payment_system.edu_payment_system'].search([]),
#         })

#     @http.route('/edu_payment_system/edu_payment_system/objects/<model("edu_payment_system.edu_payment_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edu_payment_system.object', {
#             'object': obj
#         })

