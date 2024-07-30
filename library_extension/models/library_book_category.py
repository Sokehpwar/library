# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    name = fields.Char(string="Name",
                       required=True, unique=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'The category name must be unique.')]

class LibraryBook(models.Model):
    _inherit = 'library.book'

    category_ids = fields.Many2many('library.book.category', string='Categories')
    