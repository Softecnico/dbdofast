# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Softecnico SA
#    Licence: 
#
##############################################################################
from openerp.osv import fields, osv, orm
from datatime import time, datatime
from tools.translate import _
#from openerp import tools

class clase_dbdofast(osv.osv):
    _name = "clase.dbdofast"                                                      # nombre de objeto (requerido)
    _description = "Simple Day by Day Management"                           # 
    _rec_name = 'titulo'                                                    # elegimos el campo por el cual se crean las vistas
    _columns = {                                                            #-------------------------------------------
                'titulo' : fields.char('Título', size=30, help='Este es el titulo de la ventana', required=True, translate=True),   # diccionario de campos de objeto (requerido)
                'nota' : fields.text('Nota'),                               #
                'fecha' : fields.date('Fecha', readonly=True),              #
                'active' : fields.boolean('Activo'),                        # activa o no en la vista de usuario, nombre de campo por omisión en Odoo
                'state' : fields.selection([('uno','Uno'),('dos','Dos')],'Estado'),   # campo por omision Odoo, estados seleccionables
                }                                                           #-------------------------------------------
    _defaults = {                                                           #-------------------------------------------                                                           
                 #'fecha' : lamdba *a: time.strftime('%d-%m-%Y'),
                 'state' : 'uno',                                            # diccionario de campos que contienen valores por defecto de los antes definidos
                 }                                                          #-------------------------------------------
    #_order = "id"
    #_inherit =                                                              # nombre del objeto padre que el objeto actual hereda de
    #_constraints =                                                          # lista de tuplas de las restricciones sobre el objeto
    #_sql_constraints =                                                      # lista de tuplas que define las limitaciones de SQL
    #_rec_name =                                                             # campo alternativo para utilizar como nombre
    #_auto =                                                                 # Determina si una tabla de PostgreSQL correspondiente 
                                                                             # debe ser generado de forma automática desde el objeto
clase_dbdofast()