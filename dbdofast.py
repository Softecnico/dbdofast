# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Softecnico SA
#    Licence: 
#
##############################################################################
from openerp import models, fields, api
#from datatime import time, datatime
#from tools.translate import _
#from openerp import tools

class modelo_reparto(models.Model):
    _name = 'modelo.reparto'                                                 # nombre de objeto (requerido)
    _description = 'Módulo de Gestión de Repartos'                           # 
    # diccionario de campos de objeto (requerido)
    name = fields.Char('Nombre', size=30, help='Este es el Nombre', required=True, translate=True),
    # titulo = fields.Char('Título', size=30, help='Este es el titulo de la ventana', required=True, translate=True),
    # nota = fields.Char('Nota'),                                              #
    # fecha = fields.Date('Fecha', readonly=True),                             #
    # active = fields.Boolean('Activo'),                                       # activa o no en la vista de usuario, nombre de campo por omisión en Odoo
    # state = fields.Selection([('uno','Uno'),('dos','Dos')],'Estado'),        # campo por omision Odoo, estados seleccionables
    #_columns = {                                                            #-------------------------------------------

    #            }                                                           #-------------------------------------------
    #_defaults = {                                                           #-------------------------------------------                                                           
                 #'fecha' : lamdba *a: time.strftime('%d-%m-%Y'),
    #             'state' : 'uno',                                           # diccionario de campos que contienen valores por defecto de los antes definidos
    #             }                                                          #-------------------------------------------
    #_order = "id"
    #_inherit =                                                              # nombre del objeto padre que el objeto actual hereda de
    #_constraints =                                                          # lista de tuplas de las restricciones sobre el objeto
    #_sql_constraints =                                                      # lista de tuplas que define las limitaciones de SQL
    #_rec_name =                                                             # campo alternativo para utilizar como nombre
    #_auto =                                                                 # Determina si una tabla de PostgreSQL correspondiente 
                                                                             # debe ser generado de forma automática desde el objeto
modelo_reparto()