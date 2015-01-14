# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Softecnico SA
#    Licence: 
#
##############################################################################
from openerp import models, fields

class repartidor_contrato(models.Model): # Repartidor_Tiene_ContratoReparto(...) en documentación
  _name = 'repartidor.contrato'
  _description = 'Tabla de repartidores con contrato'

  name = fields.Char('Repartidor', size=30, help='Este es el Nombre del repartidor', required=True, translate=False)
  CIF_rep = fields.Char('CIF', size=10, help='Identificación de la empresa repartidora', required=True, translate=False)
  ID_contrato_repartidor = fields.Integer('Nº de Contrato', help='Este será el ID del contrato del Repartidor')

repartidor_contrato() # aquí finaliza la clase no hace falta pero ayuda (no requerido)