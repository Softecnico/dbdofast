# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Softecnico SA
#    Licence: 
#
##############################################################################
import fields, osv
import time

class dbdofast(osv.osv):
    _name = "dbdofast"                                                      # nombre de objeto (requerido)
    _description = "Simple Day by Day Management"                           # 
    _columns = {                                                            #-------------------------------------------
                'titulo' : fields.char('Título', size=30, required=True),   # diccionario de campos de objeto (requerido)
                'nota' : fields.text('Nota'),                               #
                'fecha_nota' : fields.date('Fecha'),                        #
                }                                                           #-------------------------------------------
    #_defaults = {                                                           #-------------------------------------------                                                           
    #                                                                        # diccionario de campos que contienen valores por defecto
    #             }                                                          #-------------------------------------------
    #_inherit =                                                              # nombre del objeto padre que el objeto actual hereda de
    #_constraints =                                                          # lista de tuplas de las restricciones sobre el objeto
    #_sql_constraints =                                                      # lista de tuplas que define las limitaciones de SQL
    #_rec_name =                                                             # campo alternativo para utilizar como nombre
    #_auto =                                                                 # Determina si una tabla de PostgreSQL correspondiente 
                                                                             # debe ser generado de forma automática desde el objeto.
dbdofast()