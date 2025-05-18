# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


PATTERN = r'([\w\+\- ]*)\[([\w\+\-\. ]+)\]([\w\+\-\. ]+)'

class ProcessGroup(models.Model):
    _name = 'process.group'

    name = fields.Char(string='ID', required=True)
    date = fields.Datetime(string='Procesado', required=True)
    process_data_ids = fields.One2many('process.data', inverse_name='process_group_id', string='Data IDs')
    proyecto_normativo_ids = fields.One2many('proyecto.normativo', inverse_name='process_group_id', string='Proyectos Normativos')
    reference_date = fields.Date(string='Fecha Referencia', default=lambda self: fields.Date.today())

    def get_normativos(self):
        # Lista de proyectos con JP
        proyectos = self.env['process.proyecto'].get_proyectos_asignados()
        _logger.info('PROYECTOS: %s'%(proyectos))

        # Elimina el listado actual
        for normativo in self.proyecto_normativo_ids:
            self.proyecto_normativo_ids = [(2,normativo.id)]

        for rec in self.process_data_ids:
            proyecto = re.search(PATTERN, rec.codigo_req, flags=re.IGNORECASE)
            if proyecto:
                nombre_proyecto = proyecto.group(2).strip()
                _logger.info('PROYECTO: %s'%(nombre_proyecto))
                if nombre_proyecto in proyectos:
                    _logger.info('process_data_id %s'%(rec.id))
                    self.proyecto_normativo_ids = [(0,0,{
                        'name': nombre_proyecto,
                        'process_data_id': rec.id,
                        })]
