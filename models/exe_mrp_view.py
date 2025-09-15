from odoo import models

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    def button_finish(self):
        res = super().button_finish()
        return {
            'type': 'ir.actions.act_url',
            'url': '/mrp/workcenter_control_panel',
            'target': 'self',
        }