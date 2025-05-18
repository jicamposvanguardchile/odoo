# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProcessFeriado(models.Model):
    _name = 'process.feriado'

    name = fields.Char(string='Nombre')
    date = fields.Date(string='Fecha')
    descripcion = fields.Char(string='Descripción')
    year = fields.Integer(string='Año', compute='_compute_year')

    @api.depends('date')
    def _compute_year(self):
        for rec in self:
            if rec.date:
                rec.year = int(rec.date.strftime('%Y'))

    @api.model
    def get_feriados(self,year=False):
        Feriado = self.env['process.feriado']
        domain = [('year','=',year)] if year else []
        feriados = Feriado.search(domain).mapped('date')
        return feriados


