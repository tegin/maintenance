# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    def _create_new_request(self, maintenance_plan):
        res = super()._create_new_request(maintenance_plan)
        if maintenance_plan.plan_definition_id:
            maintenance_plan.plan_definition_id.execute_plan_definition(
                maintenance_plan._get_execute_plan_vals(res)
            )
        return res