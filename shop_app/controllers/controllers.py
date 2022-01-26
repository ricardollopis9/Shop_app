# -*- coding: utf-8 -*-
# from odoo import http


# class ShopApp(http.Controller):
#     @http.route('/shop_app/shop_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shop_app/shop_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shop_app.listing', {
#             'root': '/shop_app/shop_app',
#             'objects': http.request.env['shop_app.shop_app'].search([]),
#         })

#     @http.route('/shop_app/shop_app/objects/<model("shop_app.shop_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shop_app.object', {
#             'object': obj
#         })
