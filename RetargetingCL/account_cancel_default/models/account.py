#-*- coding:utf-8 -*-

from odoo import models, fields, api

class AccountJournal(models.Model):
    _inherit = "account.journal"   

    update_posted = fields.Boolean(default=True)