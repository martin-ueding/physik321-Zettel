#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np

__docformat__ = "restructuredtext en"

_epsilon_0 = 8.85419e-12
"""
Vacuum permittivity.
"""

_elementary_charge = 1.609e-19
"""
Elementary charge.
"""

def integers(limit=None):
    """
    Iterator that yields the integers :math:`\mathbb Z` in the order 0, 1, -1,
    2, -2, 3, ….

    :param limit: The largest integer to be returned, inclusively.
    :type limit: int
    :rtype: generator
    """
    i = 0

    yield i

    while limit is None or i < limit:
        i += 1
        yield i
        yield -i

def points(limit=None):
    """
    Iterator that goes through the three dimensional points around the origin.
    It will order the points by the uniform norm which is just the maximum of
    all the coordinates (absolute value).

    :rtype: generator
    """
    for x in integers(limit):
        for y in integers(np.abs(x)):
            for z in integers(np.abs(x)):
                yield (x, y, z)

def potential(sign, R):
    """
    Potential energy with charge ``e`` and distance ``R``.

    :param sign: How to count this charge.
    :type sign: int or float
    :return: Potential energy.
    :rtype: float
    """
    return sign * _elementary_charge**2 / (4 * np.pi * _epsilon_0 * R)

def total_potential(limit=None):
    """
    Calculates the total potential including all the points ``(a, b, c)`` where
    ``max(a, b, c) <= limit`` holds.

    :param limit: Which points to include.
    :type limit: int
    :return: Total potential energy
    :rtype: float
    """
    U = 0
    for x, y, z in points(limit):
        R = np.sqrt(x**2 + y**2 + z**2)

        if R < 0.1:
            continue

        sign = (-1)**x * (-1)**y * (-1)** z

        U += potential(sign, R)

    return U

def main():
    U = total_potential(60)

    print("U =", U, "V")

if __name__ == "__main__":
    main()
