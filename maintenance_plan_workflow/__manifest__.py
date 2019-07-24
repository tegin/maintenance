# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Maintenance Plan Workflow',
    'summary': """
        Workflows for Maintenance""",
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Creu Blanca,Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/maintenance',
    'depends': [
        'maintenance_plan',
        'workflow_activity',
    ],
    'data': [
        'views/maintenance_plan.xml',
    ],
    'demo': [
    ],
}
