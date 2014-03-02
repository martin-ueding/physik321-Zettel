// Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

/*
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */

public class H3 {
	private static double potential(int limit) {
		double U = 0.0;
		double e2 = Math.pow(1.609e-19, 2);
		double e0 = 8.85419e-12;
		double pi = Math.PI;

		int x, y, z;

		int sign;

		for (x = -limit; x <= limit; ++x) {
			for (y = -limit; y <= limit; ++y) {
				for (z = -limit; z <= limit; ++z) {
					if (x == 0 && y == 0 && z == 0) {
						continue;
					}

					sign = (x + y + z) % 2 == 0 ? 1 : -1;
					U += sign * e2 / (4 * pi * e0 * Math.sqrt(x*x + y*y + z*z));
				}
			}
		}

		return U;
	}

	public static void main(String[] args) {
		double U = potential(60);

		System.out.println("U = "+U+" J\n");
	}
}
