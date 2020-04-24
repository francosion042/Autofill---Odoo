# -*- coding: utf-8 -*-
# from odoo import http


# class Autofill(http.Controller):
#     @http.route('/autofill/autofill/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/autofill/autofill/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('autofill.listing', {
#             'root': '/autofill/autofill',
#             'objects': http.request.env['autofill.autofill'].search([]),
#         })

#     @http.route('/autofill/autofill/objects/<model("autofill.autofill"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('autofill.object', {
#             'object': obj
#         })
