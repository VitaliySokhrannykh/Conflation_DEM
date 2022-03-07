# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CounterpartStreams
                                 A QGIS plugin
 Conflation_DEM
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-03-30
        copyright            : (C) 2021 by Sokhrannykh V., Samsonov T. 
        email                : vitaliy_mapgeo@mail.ru
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Sokhrannykh V., Samsonov T. '
__date__ = '2021-03-30'
__copyright__ = '(C) 2021 by Sokhrannykh V., Samsonov T. '


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CounterpartStreams class from file CounterpartStreams.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .counterpart_streams import CounterpartStreamsPlugin
    return CounterpartStreamsPlugin()