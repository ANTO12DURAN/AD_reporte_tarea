# -*- coding: utf-8 -*-
{
    'name': "ReporteTareas",

    'summary': """ Permite generar las tareas que se deben realizar en el cultivo""",

    'description': """ 
        Genera las tareas que se deben realizar en el cultivo       
    """,

    'author': "Antonieta Duran",
    'website': "http://www.enproceso.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/tarea_view.xml',
        'views/lote_view.xml',
        'views/responsable_view.xml',
        'views/formulacion_view.xml',
        'views/tipoactividad_view.xml',
        'views/actividad_view.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #    'demo/demo.xml',
    # ],
}
