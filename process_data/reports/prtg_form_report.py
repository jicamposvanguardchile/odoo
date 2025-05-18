from odoo import models,api

import logging

_logger = logging.getLogger(__name__)

class PRTGFormReport(models.AbstractModel):
    _name = 'report.prtg_reports.prtg_form_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        _logger.info(' PRTGFormReport ')
        _logger.info(' data %s'%(data))

        if not docids:
            docids = [self.env.context.get('active_id')]

        docs = self.env['prtg.report'].browse(docids)
        _logger.info(docids)
        _logger.info(docs)
        return {
            'doc_ids': docids,
            'doc_model': 'prtg.report',
            'docs': docs,
            'data': data,
        }
