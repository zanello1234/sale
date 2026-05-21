##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _is_not_sellable_line(self):
        """Return True for lines that can't be sold independently in the cart.

        Covers section/note display lines and product pack component lines.
        """
        return bool(self.display_type) or bool(getattr(self, "pack_parent_line_id", False))
