"""
 eqip

                             -------------------
        begin                : 2022-05-23
        copyright            : (C) 2022 by Alexandra Institute
        email                : christian.heider@alexandra.dk
        git sha              : $Format:%H$

"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load eqip class from file eqip.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .plugin import Eqip

    return Eqip(iface)
