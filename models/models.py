# -*- coding: utf-8 -*-
import requests
from odoo import models, fields, api

users = requests.get('https://jsonplaceholder.typicode.com/users').json()


class autofill(models.Model):
    _name = 'autofill.autofill'
    _description = 'autofill form fields'

    autofill_id = fields.Integer(string="ID")
    autofill_name = fields.Char(string="Full Name")
    autofill_username = fields.Char(string="Username")
    autofill_email = fields.Char(string="E-mail")
    autofill_phone = fields.Char(string="Phone")

    @api.onchange('autofill_id')
    def get_details(self):
        for user in users:
            if self.autofill_id == user['id']:
                self.autofill_name = user['name']
                self.autofill_username = user['username']
                self.autofill_email = user['email']
                self.autofill_phone = user['phone']

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
