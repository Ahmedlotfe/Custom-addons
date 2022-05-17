# -*- coding: utf-8 -*-
# from odoo import http


# class CustomContact(http.Controller):
#     @http.route('/custom_contact/custom_contact', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_contact/custom_contact/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_contact.listing', {
#             'root': '/custom_contact/custom_contact',
#             'objects': http.request.env['custom_contact.custom_contact'].search([]),
#         })

#     @http.route('/custom_contact/custom_contact/objects/<model("custom_contact.custom_contact"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_contact.object', {
#             'object': obj
#         })
