# -*- coding: utf-8 -*-
# from odoo import http


# class CustomHospital(http.Controller):
#     @http.route('/custom_hospital/custom_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_hospital/custom_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_hospital.listing', {
#             'root': '/custom_hospital/custom_hospital',
#             'objects': http.request.env['custom_hospital.custom_hospital'].search([]),
#         })

#     @http.route('/custom_hospital/custom_hospital/objects/<model("custom_hospital.custom_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_hospital.object', {
#             'object': obj
#         })
