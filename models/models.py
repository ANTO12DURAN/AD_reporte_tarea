# -*- coding: utf-8 -*-

from odoo import models, fields


class ReporteTarea(models.Model):
    _name = "reporte.tarea"  # tabla de bd => reporte_tarea
    _description = "Reporte Tarea"

    name = fields.Char(string="Tarea", required=True, )
    date_form = fields.Datetime(string="Starting Date", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="End Date", required=False, )

    lote_id = fields.Many2one(comodel_name="reporte.lote", string="lote", required=True, )


#    formulacion_ids = fields.One2many('reporte.formulacion', inverse_name='reportetarea_id', string='reporte.formulacion', )

class lote(models.Model):
    _name = "reporte.lote"  # table de bd => reporte_lote
    _description = "Lotes"

    name = fields.Char(string="Lote", required=True)
    description = fields.Char(string="Description", required=True)
    reportetarea_ids = fields.One2many('reporte.tarea', inverse_name='lote_id', string='Tarea', )


class responsable(models.Model):
    _name = "reporte.responsable"  # tabla de bd => reporte_responsable
    _description = "Responsable"

    name = fields.Char(string="Responsable", required=True, )
    description = fields.Char(string="Description", required=True, )
    employee_id = fields.Many2one(comodel_name="hr.employee", string="empleado", required=True, )
    # actividad_id =fields.Many2one(comodel_name="reporte.actividad", string="actividad", required=True, )


class formulacion(models.Model):
    _name = "reporte.formulacion"  # tabla de bd => reporte_formulacion
    _description = "Formulacion"

    name = fields.Char(string="Formulacion", required=True)
    description = fields.Char(string="Description", required=True, )
    # reportetarea_id = fields.Many2one(comodel_name="reporte_tarea", string="tarea", required=True, )
    # product_id = fields.Many2one(comodel_name="product.product", string="producto", required=True, )


class TipoActividad(models.Model):
    _name = "reporte.tipoactividad"  # tabla de bd => reporte_tipoactividad
    _description = "TipoActividad"

    name = fields.Char(string="Tipo Actividad", required=True)
    description = fields.Char(string="description", required=True)
    actividad_ids = fields.One2many('reporte.actividad', inverse_name='tipoactividad_id', string='Actividad')


class Actividad(models.Model):
    _name = "reporte.actividad"
    _description = "Actividad"

    name = fields.Char(string="Actividad", required=True)
    description = fields.Char(string="description", required=True)
    tipoactividad_id = fields.Many2one(comodel_name="reporte.tipoactividad", string="Tipo Actividad", required=True, )
    #responsable_ids = fields.One2many('reporte.responsable', inverse_name='actividad_id', string='reporte.responsable')
