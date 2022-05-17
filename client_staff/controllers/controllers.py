# -*- coding: utf-8 -*-
# from odoo import http


# class ClientStaff(http.Controller):
#     @http.route('/client_staff/client_staff', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/client_staff/client_staff/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('client_staff.listing', {
#             'root': '/client_staff/client_staff',
#             'objects': http.request.env['client_staff.client_staff'].search([]),
#         })

#     @http.route('/client_staff/client_staff/objects/<model("client_staff.client_staff"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('client_staff.object', {
#             'object': obj
#         })
