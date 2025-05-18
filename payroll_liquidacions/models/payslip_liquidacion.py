from odoo import models, api

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    @api.depends('worked_days_line_ids.number_of_days', 'contract_id.wage')
    def compute_liquidacion(self):
        for slip in self:
            daily_wage = slip.contract_id.wage / 30 if slip.contract_id.wage else 0
            total_days = sum(slip.worked_days_line_ids.mapped('number_of_days'))
            slip.amount = daily_wage * total_days
