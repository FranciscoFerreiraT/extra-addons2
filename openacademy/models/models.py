# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TestModel(models.Model):
    _name = 'test_model' # Nombre de la tabla
    _description = 'Test Model' # Descripcion de la tabla

    name = fields.Char(string='Name', required=True) # nombre del campo (name) y que tipo es + si es requerido
    description = fields.Text() # nombre del campo (descripcion) y que tipo es

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
