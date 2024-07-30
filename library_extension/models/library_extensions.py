# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryExtensions(models.Model):
    _inherit = 'library.book'

    author_id = fields.Many2one('res.partner', string='Author', ondelete='cascade', required=True)
