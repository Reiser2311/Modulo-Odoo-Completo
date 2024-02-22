# -*- coding: utf-8 -*-

from odoo import models, fields, api


class director(models.Model):
    _name = 'video_club.director'
    _description = 'video_club.director'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre')
    imagen = fields.Binary(string="Imagen")
    anyoNacimiento = fields.Date(string='Año Nacimiento')
    anyosActivo = fields.Integer(string='Años en activo')
    pelis = fields.One2many('video_club.peliculas', 'director', string='Peliculas')

class peliculas(models.Model):
    _name = 'video_club.peliculas'
    _description = 'video_club.peliculas'
    _rec_name = 'titulo'

    titulo = fields.Char(string='Titulo')
    imagen = fields.Binary(string="Imagen")
    duracion = fields.Integer(string='Duracion(min)')
    presupuesto = fields.Integer(string='Presupuesto')
    recaudacion = fields.Integer(string='Recaudacion')
    valoracion = fields.Char(string='Valoracion')
    director = fields.Many2one('video_club.director', string='Director')
    actores = fields.Many2many('video_club.actores')

class actores(models.Model):
    _name = 'video_club.actores'
    _description = 'video_club.actores'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre')
    imagen = fields.Binary(string="Imagen")
    anyoNacimiento = fields.Date(string='Año nacimiento')
    anyosActivo = fields.Integer(string='Años en activo')
    peliculas = fields.Many2many('video_club.peliculas')
    premios = fields.One2many('video_club.premios', 'ganador', string='Premios')

class premios(models.Model):
    _name = 'video_club.premios'
    _description = 'video_club.premios'
    _rec_name = 'titulo'

    titulo = fields.Char(string='Titulo')
    anyo = fields.Date(string='Año')
    ganador = fields.Many2one('video_club.actores', string='Ganador')