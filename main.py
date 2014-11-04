# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Softecnico SA
#    Licence: 
#
##############################################################################

from openerp.osv import osv, fields
from openerp.tools.translate import _

class note_pad_note(osv.osv):
    """ memo pad """

    _name = 'note.note'
    _inherit = ['pad.common','note.note']

    _pad_fields = ['note_pad']

    _columns = {
        'note_pad_url': fields.char('Pad Url', pad_content_field='memo'),
    }