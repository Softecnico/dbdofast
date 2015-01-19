# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Softecnico SA
#    Licence: 
#
##############################################################################
from openerp import models, fields

class realiza_reparto(models.Model): # Repartidor_Tiene_ContratoReparto(...) en documentación
  _name = 'realiza.reparto'
  _description = 'Tabla de repartos a realizar'

  name = fields.Integer('Reparto', help='Este es el numero de orden de reparto', required=True, translate=False)
  CIF_rep = fields.Many2one('repartidor.contrato')
  ID_factura = fields.Integer('Nº de Factura', help='Este será el ID de la Factura')

realiza_reparto() # aquí finaliza la clase no hace falta pero ayuda (no requerido)