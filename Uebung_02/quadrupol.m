#!/usr/bin/octave -q
# Copyright © 2012 Martin Ueding <dev@martin-ueding.de>

d = 2;
e = 1;

# Liste der $\vec r_i$.
r = [
[0 d 0]
[0 -d 0]
[0 0 d]
[0 0 -d]
[-d 0 0]
[-d/2 0 0]
[d 0 0]
[2*d 0 0]
];

# Errechne den Schwerpunkt $\vec s$.
s = mean(r);

# Liste der $q_i$.
q = [e e e e -e -e -e -e];

# Initialisiere $\tens Q$.
Q = zeros(3, 3);

for k = 1:length(r)
	# Errechne den Differenzvektor $\vec x$.
	x = r(k, :) - s;

	Q += q(k) * (3 * x' * x - ones(3, 3) * norm(x)^2);
end

Q

Q*4
