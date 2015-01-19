# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Softecnico SA
#    Licence: 
#
##############################################################################
from openerp import models, fields

def _get_image(self, cr, uid, ids, name, args, context=None):
	result = dict.fromkeys(ids, False)
	for obj in self.browse(cr, uid, ids, context=context):
	    result[obj.id] = tools.image_get_resized_images(obj.image)
	return result

def _set_image(self, cr, uid, id, name, value, args, context=None):
    return self.write(cr, uid, [id], {'image': tools.image_resize_image_big(value)}, context=context)

class repartidor_contrato(models.Model): # Repartidor_Tiene_ContratoReparto(...) en documentación
	_name = 'repartidor.contrato'
	_description = 'Tabla de repartidores con contrato'

	# Campo Nombre
	name = fields.Char('Repartidor', size=30, help='Este es el Nombre del repartidor', required=True, translate=False)
	
	# Campo CIF
	CIF_rep = fields.Char('CIF', size=10, help='Identificación de la empresa repartidora', required=True, translate=False)

	# Campo estado de la barra de estado en los formularios
	state = fields.Selection([('uno','Uno'),('dos','Dos'),('tres','Tres'),('cuatro','Cuatro')],'Estado')

	# Campo Imágen grande
	image = fields.Binary('Imágen', help='Este campo contiene la imagen utilizada como foto para el empleado, limitado a 1024x1024px.')
	
	# Campo Imágen mediana
	# image_medium = fields.function(_get_image, fnct_inv=_set_image, string='Imágen mediana', type='binary', multi='_get_image', store = {'repartidor.contrato': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),},
	# help='Imagen de tamaño medio del repartidor. Será automaticamente '\
	# 'redimensionada a un tamaño de 128x128px , preservando el aspecto. '\
	# 'Esta imagen se usará en las vistas de cuadrados.')
	
	# Campo Imágen pequeña
	# image_small = fields.function(_get_image, fnct_inv=_set_image, string='Imágen pequeña', type='binary', multi='_get_image', store = {'repartidor.contrato': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),},
	# help='Imagen de tamaño pequeño del repartidor. Será automaticamente '\
	# 'redimensionada a un tamaño de 64x64px, preservando el aspecto. '\
	# 'Esta imagen será usada en cualquier sitio que sea necesaria una imagen pequeña.')
	
	# Campo ID del contrato
	ID_contrato_repartidor = fields.Integer('Nº de Contrato', help='Este será el ID del contrato del Repartidor')

repartidor_contrato() # aquí finaliza la clase no hace falta pero ayuda (no requerido)