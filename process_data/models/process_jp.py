# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProcessJefeProyecto(models.Model):
    _name = 'process.jp'

    name = fields.Char(string='Nombre')
    proyecto_ids = fields.Many2many('process.proyecto',string='Proyectos asignados')
