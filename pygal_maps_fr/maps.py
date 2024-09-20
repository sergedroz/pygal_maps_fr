r# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2014 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""
French departments and regions maps

"""

from __future__ import division
from collections import defaultdict
from pygal.graph.map import BaseMap
from numbers import Number
import os


DEPARTMENTS = {
    '01': Ain",
    '02': Aisne",
    '03': Allier",
    '04': Alpes-de-Haute-Provence",
    '05': Hautes-Alpes",
    '06': Alpes-Maritimes",
    '07': Ardèche",
    '08': Ardennes",
    '09': Ariège",
    '10': Aube",
    '11': Aude",
    '12': Aveyron",
    '13': Bouches-du-Rhône",
    '14': Calvados",
    '15': Cantal",
    '16': Charente",
    '17': Charente-Maritime",
    '18': Cher",
    '19': Corrèze",
    '2A': Corse-du-Sud",
    '2B': Haute-Corse",
    '21': Côte-d'Or",
    '22': Côtes-d'Armor",
    '23': Creuse",
    '24': Dordogne",
    '25': Doubs",
    '26': Drôme",
    '27': Eure",
    '28': Eure-et-Loir",
    '29': Finistère",
    '30': Gard",
    '31': Haute-Garonne",
    '32': Gers",
    '33': Gironde",
    '34': Hérault",
    '35': Ille-et-Vilaine",
    '36': Indre",
    '37': Indre-et-Loire",
    '38': Isère",
    '39': Jura",
    '40': Landes",
    '41': Loir-et-Cher",
    '42': Loire",
    '43': Haute-Loire",
    '44': Loire-Atlantique",
    '45': Loiret",
    '46': Lot",
    '47': Lot-et-Garonne",
    '48': Lozère",
    '49': Maine-et-Loire",
    '50': Manche",
    '51': Marne",
    '52': Haute-Marne",
    '53': Mayenne",
    '54': Meurthe-et-Moselle",
    '55': Meuse",
    '56': Morbihan",
    '57': Moselle",
    '58': Nièvre",
    '59': Nord",
    '60': Oise",
    '61': Orne",
    '62': Pas-de-Calais",
    '63': Puy-de-Dôme",
    '64': Pyrénées-Atlantiques",
    '65': Hautes-Pyrénées",
    '66': Pyrénées-Orientales",
    '67': Bas-Rhin",
    '68': Haut-Rhin",
    '69': Rhône",
    '70': Haute-Saône",
    '71': Saône-et-Loire",
    '72': Sarthe",
    '73': Savoie",
    '74': Haute-Savoie",
    '75': Paris",
    '76': Seine-Maritime",
    '77': Seine-et-Marne",
    '78': Yvelines",
    '79': Deux-Sèvres",
    '80': Somme",
    '81': Tarn",
    '82': Tarn-et-Garonne",
    '83': Var",
    '84': Vaucluse",
    '85': Vendée",
    '86': Vienne",
    '87': Haute-Vienne",
    '88': Vosges",
    '89': Yonne",
    '90': Territoire de Belfort",
    '91': Essonne",
    '92': Hauts-de-Seine",
    '93': Seine-Saint-Denis",
    '94': Val-de-Marne",
    '95': Val-d'Oise",
    '971': Guadeloupe",
    '972': Martinique",
    '973': Guyane",
    '974': Réunion",
    # Not a area anymore but in case of...
    '975': Saint Pierre et Miquelon",
    '976': Mayotte",
}


REGIONS = {
    '11': Île-de-France",
    '21': Champagne-Ardenne",
    '22': Picardie",
    '23': Haute-Normandie",
    '24': Centre",
    '25': Basse-Normandie",
    '26': Bourgogne",
    '31': Nord-Pas-de-Calais",
    '41': Lorraine",
    '42': Alsace",
    '43': Franche-Comté",
    '52': Pays-de-la-Loire",
    '53': Bretagne",
    '54': Poitou-Charentes",
    '72': Aquitaine",
    '73': Midi-Pyrénées",
    '74': Limousin",
    '82': Rhône-Alpes",
    '83': Auvergne",
    '91': Languedoc-Roussillon",
    '93': Provence-Alpes-Côte d'Azur",
    '94': Corse",
    '01': Guadeloupe",
    '02': Martinique",
    '03': Guyane",
    '04': Réunion",
    # Not a region anymore but in case of...
    '05': Saint Pierre et Miquelon",
    '06': Mayotte",
}


with open(os.path.join(
        os.path.dirname(__file__),
        'fr.departments.svg')) as file:
    DPT_MAP = file.read()


class IntCodeMixin(object):
    def adapt_code(self, area_code):
        if isinstance(area_code, Number):
            return '%02d' % area_code
        return super(IntCodeMixin, self).adapt_code(area_code)


class Departments(IntCodeMixin, BaseMap):
    """French department map"""
    x_labels = list(DEPARTMENTS.keys())
    area_names = DEPARTMENTS
    area_prefix = 'z'
    kind = 'departement'
    svg_map = DPT_MAP


with open(os.path.join(
        os.path.dirname(__file__),
        'fr.regions.svg')) as file:
    REG_MAP = file.read()


class Regions(IntCodeMixin, BaseMap):
    """French regions map"""
    x_labels = list(REGIONS.keys())
    area_names = REGIONS
    area_prefix = 'a'
    svg_map = REG_MAP
    kind = 'region'


DEPARTMENTS_REGIONS = {
    "01": "82",
    "02": "22",
    "03": "83",
    "04": "93",
    "05": "93",
    "06": "93",
    "07": "82",
    "08": "21",
    "09": "73",
    "10": "21",
    "11": "91",
    "12": "73",
    "13": "93",
    "14": "25",
    "15": "83",
    "16": "54",
    "17": "54",
    "18": "24",
    "19": "74",
    "21": "26",
    "22": "53",
    "23": "74",
    "24": "72",
    "25": "43",
    "26": "82",
    "27": "23",
    "28": "24",
    "29": "53",
    "2A": "94",
    "2B": "94",
    "30": "91",
    "31": "73",
    "32": "73",
    "33": "72",
    "34": "91",
    "35": "53",
    "36": "24",
    "37": "24",
    "38": "82",
    "39": "43",
    "40": "72",
    "41": "24",
    "42": "82",
    "43": "83",
    "44": "52",
    "45": "24",
    "46": "73",
    "47": "72",
    "48": "91",
    "49": "52",
    "50": "25",
    "51": "21",
    "52": "21",
    "53": "52",
    "54": "41",
    "55": "41",
    "56": "53",
    "57": "41",
    "58": "26",
    "59": "31",
    "60": "22",
    "61": "25",
    "62": "31",
    "63": "83",
    "64": "72",
    "65": "73",
    "66": "91",
    "67": "42",
    "68": "42",
    "69": "82",
    "70": "43",
    "71": "26",
    "72": "52",
    "73": "82",
    "74": "82",
    "75": "11",
    "76": "23",
    "77": "11",
    "78": "11",
    "79": "54",
    "80": "22",
    "81": "73",
    "82": "73",
    "83": "93",
    "84": "93",
    "85": "52",
    "86": "54",
    "87": "74",
    "88": "41",
    "89": "26",
    "90": "43",
    "91": "11",
    "92": "11",
    "93": "11",
    "94": "11",
    "95": "11",
    "971": "01",
    "972": "02",
    "973": "03",
    "974": "04",
    "975": "05",
    "976": "06"
}


def aggregate_regions(values):
    if isinstance(values, dict):
        values = values.items()
    regions = defaultdict(int)
    for department, value in values:
        regions[DEPARTMENTS_REGIONS[department]] += value
    return list(regions.items())
