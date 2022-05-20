# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalModule(http.Controller):
#     @http.route('/hospital_module/hospital_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_module/hospital_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_module.listing', {
#             'root': '/hospital_module/hospital_module',
#             'objects': http.request.env['hospital_module.hospital_module'].search([]),
#         })

#     @http.route('/hospital_module/hospital_module/objects/<model("hospital_module.hospital_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_module.object', {
#             'object': obj
#         })
