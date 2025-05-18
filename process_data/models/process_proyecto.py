# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProcessProyecto(models.Model):
    _name = 'process.proyecto'

    name = fields.Char(string='Nombre')
    alias = fields.Char(string='Alias', help='Listado de alias separados por coma')
    jp_ids = fields.Many2many('process.jp',string='Jefes de Proyectos asignados')

    @api.model
    def get_proyectos_asignados(self):
        proyecto_list = []

        proyectos = self.env['process.proyecto'].search([])
        for proyecto in proyectos: 
            if len(proyecto.jp_ids) > 0:
                proyecto_list.append(proyecto.name)
                if proyecto.alias:
                    proyecto_list.extend(proyecto.alias.split(','))
        return proyecto_list

