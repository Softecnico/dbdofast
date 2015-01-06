# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Softecnico SA
#    Licence: 
#
##############################################################################

{
    "name": "Pequeño Comercio",
    "version": "0.1",
    "category": "Generic Modules/Others",
    "description": """
Este modulo sirve para poder administrar un pequeño comercio
=================================================================

Lo que intentamos hacer con este modulo es una pantalla de gestión
para poder administrar rapidamente los datos básicos de un comercio pequeño

""",
    "author": "Softecnico S.A.",
    "website": "https://www.sudano.net",
    "summary": "Ayuda a la pequeña empresa",
    "depends": ["base"],
    "data": ["views/dbdofast_view.xml"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
        "views/dbdofast_view.xml",
        ],
    "active": False,
    "installable": True,
    "application": True,
    "auto_install": False
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
