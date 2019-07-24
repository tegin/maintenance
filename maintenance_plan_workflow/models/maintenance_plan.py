# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MaintenancePlan(models.Model):
    _inherit = 'maintenance.plan'

    plan_definition_id = fields.Many2one(
        'workflow.plan.definition',
    )

    def _get_execute_plan_vals(self, request):
        return {
            'res_model_id': self.env['ir.model'].search(
                [('model', '=', request._name)]).id,
            'res_id': request.id,
        }
