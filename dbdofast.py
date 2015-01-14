# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Softecnico SA
#    Licence: 
#
##############################################################################
from openerp import models, fields

class modelo_reparto(models.Model):
  _name = 'modelo.reparto' # nombre de objeto (requerido)
  _description = 'Modulo de Gestion de Repartos'
  
  # diccionario de campos de objeto (requerido)
  name = fields.Char('Nombre', size=30, help='Este es el Nombre', required=True, translate=True)
  titulo = fields.Char('Titulo', size=30, help='Este es el titulo de la ventana', required=True, translate=True)
  fecha = fields.Date('Fecha', readonly=True)
  estado = fields.Selection([('uno','Uno'),('dos','Dos')],'Estado')

modelo_reparto() # aquí finaliza la clase no hace falta pero ayuda (no requerido)