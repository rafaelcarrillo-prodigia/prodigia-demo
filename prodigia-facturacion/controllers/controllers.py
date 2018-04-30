# -*- coding: utf-8 -*-
from odoo import http

# class Prodigia-facturacion(http.Controller):
#     @http.route('/prodigia-facturacion/prodigia-facturacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prodigia-facturacion/prodigia-facturacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prodigia-facturacion.listing', {
#             'root': '/prodigia-facturacion/prodigia-facturacion',
#             'objects': http.request.env['prodigia-facturacion.prodigia-facturacion'].search([]),
#         })

#     @http.route('/prodigia-facturacion/prodigia-facturacion/objects/<model("prodigia-facturacion.prodigia-facturacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prodigia-facturacion.object', {
#             'object': obj
#         })