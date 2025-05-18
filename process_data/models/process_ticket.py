# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProcessTicket(models.Model):
    _name = 'process.ticket'
    _name_rec = 'code'

    code = fields.Char(string='Código')
    resumen = fields.Text(string='Resumen')
    categ_id = fields.Many2one('process.ticket.categ',string='Categoría')
