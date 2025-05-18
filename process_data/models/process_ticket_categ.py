# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProcessTicketCateg(models.Model):
    _name = 'process.ticket.categ'

    name = fields.Char(string='Nombre')
    ticket_ids = fields.One2many('process.ticket', 'categ_id', string='Tickets')

