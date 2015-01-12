# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Softecnico SA
#    Licence: 
#
##############################################################################
from openerp.osv import osv, fields
#from datatime import time, datatime
#from tools.translate import _
#from openerp import tools

class modelo_reparto(osv.osv):
    _name = 'modelo.reparto'                                                 # nombre de objeto (requerido)
    _description = 'Modulo de Gestion de Repartos'                           #

    # diccionario de campos de objeto (requerido)
    _columns = {                                                              #-------------------------------------------
      'name' : fields.char('Nombre', size=30, help='Este es el Nombre', required=True, translate=True),
      'titulo' : fields.char('Titulo', size=30, help='Este es el titulo de la ventana', required=True, translate=True),
      'fecha' : fields.date('Fecha', readonly=True),                          # Campo de tipo fecha y de solo lectura
      'estado' : fields.selection([('uno','Uno'),('dos','Dos')],'Estado'),    # campo por omision Odoo, estados seleccionables
      #'active' : fields.boolean(True),                                        # Activa la el modelo para que sea visible
    }                                                                         #-------------------------------------------

    # _defaults = {                                                             #-------------------------------------------                                                           
    #              'fecha' : lamdba *a: time.strftime('%d-%m-%Y'),              # diccionario de campos que contienen 
    #              'estado' : 'uno',                                            # valores por defecto de los antes definidos
    # }                                                                         #-------------------------------------------
    
    #_order = "id"
    #_inherit =                                                               # nombre del objeto padre que el objeto actual hereda de
    #_constraints =                                                           # lista de tuplas de las restricciones sobre el objeto
    #_sql_constraints =                                                       # lista de tuplas que define las limitaciones de SQL
    #_rec_name =                                                              # campo alternativo para utilizar como nombre
    #_auto =                                                                  # Determina si una tabla de PostgreSQL correspondiente 
                                                                              # debe ser generado de forma automática desde el objet