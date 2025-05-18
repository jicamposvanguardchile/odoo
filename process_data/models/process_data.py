# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ProcessData(models.Model):
    _name = 'process.data'

    process_group_id = fields.Many2one('process.group', string='Process Group')
    codigo_req     = fields.Char(string='Codigo Requerimiento')
    numero_de_os   = fields.Char(string='Numero de OS')
    estado_os      = fields.Char(string='Estado OS')
    fecha_apertura = fields.Datetime(string='Fecha de Apertura')
    fecha_comprometida = fields.Datetime(string='Fecha Comprometida')
    fecha_test         = fields.Datetime(string='Fecha en TEST')
    fecha_finalizacion = fields.Datetime(string='Fecha Real de Finalización')
    hh_estimadas = fields.Float(string='H/H Estimadas')
    hh_cotizada = fields.Float(string='H/H Cotizada')
    grupo_responsable = fields.Char(string='Grupo Solucion Responsable')
    categoria = fields.Char(string='Categoria')
    tipo = fields.Char(string='Tipo')
    descripcion = fields.Text(string='Descripción Requerimiento')
    respuesta = fields.Text(string='Respuesta')
    fecha_produccion = fields.Datetime(string='Fecha Paso Producción')
    fecha_pendiente = fields.Datetime(string='Fecha Pendiente AFP')
    fecha_test_aprobado = fields.Datetime(string='Fecha Test Aprobado')
    fecha_ultima_iteracion = fields.Datetime(string='Fecha Ultima Iteración')
    fecha_usuario_compromiso = fields.Datetime(string='Fecha Usuario Compromiso')
    hh_administracion_jp = fields.Float(string='HH Administración JP')
    hh_analisis = fields.Float(string='HH Analisis')
    hh_construccion = fields.Float(string='HH Construcción')
    hh_correcciones = fields.Float(string='HH Correcciones')
    hh_diseno = fields.Float(string='HH Diseño')
    hh_instalacion = fields.Float(string='HH Instalación')
    hh_pruebas = fields.Float(string='HH Pruebas')
    fecha_ingreso_moebius = fields.Datetime(string='Fecha Ingreso Moebius')
    analista_resp_sonda = fields.Char(string='Analista Responsable SONDA')
    departamento_usuario = fields.Char(string='Departamento Usuario')
    agente_resp_apf = fields.Char(string='Agente Responsable AFP')
    tipo_solicitud = fields.Char(string='Tipo de solicitud')
    prioridad = fields.Char(string='Prioridad')
    fecha_hora_atencion = fields.Datetime(string='Fecha hora atención')
    fecha_hora_transferencia = fields.Datetime(string='Fecha hora primera transferencia')
    area_usuario = fields.Char(string='Area de Usuario')
    reporte_cliente = fields.Char(string='Reporte Cliente')

    proyecto_normativo_ids = fields.One2many('proyecto.normativo', 'process_data_id', string='Proy. Normativo')

