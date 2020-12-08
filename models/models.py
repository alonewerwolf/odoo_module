# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Footballer(models.Model):
    _name = 'my_module.footballer'
    _description = 'Footballers'
    # _inherit = 'project.project'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer('Age')
    image = fields.Binary(string='Image')
    description = fields.Text()
    footballer_number = fields.Integer('Number')
    footballer_id = fields.Many2one('my_module.football_club')


class FootballClub(models.Model):
    _name = 'my_module.football_club'
    _description = 'Football Club'

    image = fields.Binary(string='Image')
    football_club = fields.Char(string="FC", required=True)
    description = fields.Text()
    fc_id = fields.One2many('my_module.footballer', 'footballer_id')
