# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import logging
import datetime
import numpy as np

_logger = logging.getLogger(__name__)



class ProyectoNormativo(models.Model):
    _name = 'proyecto.normativo'

    name = fields.Char(string='Proyecto', required=True, index=True)
    process_group_id = fields.Many2one('process.group', string="Grupo")
    process_data_id  = fields.Many2one('process.data', string="Data original")
    numero_de_os   = fields.Char(related='process_data_id.numero_de_os')
    fecha_apertura = fields.Datetime(related='process_data_id.fecha_apertura', store=True)
    periodo_ini = fields.Char(string='Período INI', compute='_compute_periodo_ini', store=True)
    fecha_finalizacion = fields.Datetime(related='process_data_id.fecha_finalizacion', store=True)
    periodo_fin = fields.Char(string='Período FIN', compute='_compute_periodo_fin', store=True)
    fecha_usuario_compromiso = fields.Datetime(related='process_data_id.fecha_usuario_compromiso', store=True)
    atrasos = fields.Integer(string='Atrasos', compute='_compute_atrasos', store=True)
    mismo_mes = fields.Boolean(string='Mismo MES', compute='_compute_mismo_mes', store=True)

    prioridad = fields.Boolean(string='Prioridad', compute='_compute_prioridad', store=True)


    @api.depends('process_data_id')
    def _compute_prioridad(self):
        tickets = self.env['process.ticket'].search([]).mapped('code')
        #_logger.info('PRIORIDAD %s'%(tickets))
        for rec in self:
            #_logger.info('REC %s'%(rec.numero_de_os))
            if rec.numero_de_os in tickets:
                rec.prioridad = True
            else:
                rec.prioridad = False

    @api.depends('fecha_apertura')
    def _compute_periodo_ini(self):
        for rec in self:
            if rec.fecha_apertura:
                rec.periodo_ini = rec.fecha_apertura.strftime('%Y%m')

    @api.depends('fecha_finalizacion')
    def _compute_periodo_fin(self):
        for rec in self:
            #_logger.info('TICKET %s FECHA %s'%(rec.numero_de_os,rec.fecha_finalizacion))
            if rec.fecha_finalizacion:
                rec.periodo_fin = rec.fecha_finalizacion.strftime('%Y%m')

    @api.depends('fecha_usuario_compromiso','process_group_id.reference_date')
    def _compute_atrasos(self):
        feriados = self.env['process.feriado'].get_feriados()

        for rec in self:
            if rec.fecha_usuario_compromiso:
                start = rec.fecha_usuario_compromiso.date()
                end = rec.process_group_id.reference_date

                days = np.busday_count(start, end, holidays=feriados)
                rec.atrasos = days

    @api.depends('periodo_ini','periodo_fin')
    def _compute_mismo_mes(self):
        for rec in self:
            if rec.periodo_ini and rec.periodo_fin:
                if rec.periodo_ini == rec.periodo_fin:
                    rec.mismo_mes = True
                else:
                    rec.mismo_mes = False
