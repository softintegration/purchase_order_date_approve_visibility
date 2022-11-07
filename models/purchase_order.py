# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from functools import partial
from itertools import groupby
import json

from markupsafe import escape, Markup
from pytz import timezone, UTC
from werkzeug.urls import url_encode

from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang, format_amount


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    date_approve = fields.Datetime('Confirmation Date', readonly=False, index=True, copy=False,
                                   states={'cancel': [('readonly', True)], 'done': [('readonly', True)],'purchase': [('readonly', True)]})

    def button_approve(self, force=False):
        date_approve_by_order = {}
        for each in self:
            if each.date_approve:date_approve_by_order.update({each.id:each.date_approve})
        res = super(PurchaseOrder, self).button_approve(force=force)
        #FIXME:we have to discuss this solutions from performance point of view (send sql query as many as records in rcordset is bad,bu is the ORM take in care this?)
        for each in self:
            each.write({"date_approve":date_approve_by_order.get(each.id)})
        return res