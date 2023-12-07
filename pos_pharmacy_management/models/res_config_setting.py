# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_add_pos_menu = fields.Boolean(string="Add a Menu Bar")
    is_pos_advance_search = fields.Boolean(string="Advance Search")
    is_show_product_manu = fields.Boolean(string="Is Show Detail Product Manufacturer")
    is_storage_show = fields.Boolean(string="Is Storage Detail Show")
    is_medicine_use = fields.Boolean(string="Use Of Medicine")
    is_salt_alter = fields.Boolean(string="Salt Alternate")
    is_salt_comp = fields.Boolean(string="Salt Composition")
    is_substitute = fields.Boolean(string="Substitute")
    is_side_effect = fields.Boolean(string="Side Effects")
    is_safety_advice = fields.Boolean(string="Safety Advice")
    is_basic_salt = fields.Boolean(string="Basic Salt")
    is_show_medicine_info = fields.Boolean(string="Medicine Info")
    is_quick_pay_button = fields.Boolean(string="Quick Pay Button")




