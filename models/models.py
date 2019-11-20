# -*- coding: utf-8 -*-

from odoo import models, fields


class ReporteTarea(models.Model):
    _name = "reporte.tarea"  # tabla de bd => reporte_tarea
    _description = "Reporte Tarea"

    name = fields.Char(string="Tarea", required=True, )
    date_form = fields.Datetime(string="Starting Date", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="End Date", required=False, )
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    product_id = fields.Many2one(comodel_name="product.product", string="producto", required=True, )
    lote_id = fields.Many2one(comodel_name="reporte.lote", string="lote", required=True, )


class lote(models.Model):
    _name = "reporte.lote"
    _description = "Lotes"

    name = fields.Char(string="Lote", required=True)
    description = fields.Char(string="Description", required=True)
    reportetarea_ids = fields.One2many('reporte.tarea', inverse_name='lote_id', string='reporte.tarea', )
