# -*- coding: utf-8 -*-

# class ReporteTareas(http.Controller):
#     @http.route('/reporte_tareas/reporte_tareas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reporte_tareas/reporte_tareas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reporte_tareas.listing', {
#             'root': '/reporte_tareas/reporte_tareas',
#             'objects': http.request.env['reporte_tareas.reporte_tareas'].search([]),
#         })

#     @http.route('/reporte_tareas/reporte_tareas/objects/<model("reporte_tareas.reporte_tareas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reporte_tareas.object', {
#             'object': obj
#         })
