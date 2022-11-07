# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    date_approve = fields.Datetime('Confirmation Date', readonly=False, index=True, copy=False,
                                   states={'cancel': [('readonly', True)], 'done': [('readonly', True)],'purchase': [('readonly', True)]})

    def button_approve(self, force=False):
        date_approve_by_order = {}
        for each in self:
            if each.date_approve:date_approve_by_order.update({each.id:each.date_approve})
        res = super(PurchaseOrder, self).button_approve(force=force)
        #FIXME:we have to discuss this solutions from performance point of view (send sql query as many as records in rcordset is bad,
        # but is the ORM take in care this?),however this solution ensure the call the super method which is crucial
        for each in self:
            each.write({"date_approve":date_approve_by_order.get(each.id)})
        return res