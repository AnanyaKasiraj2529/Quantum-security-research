# attack_models.py

import numpy as np
from bb84 import generate_bases, measure_qubits


def eve_intercept(qubits):
    n = len(qubits)
    eve_bases = generate_bases(n)

    # Eve measures
    eve_bits = measure_qubits(qubits, eve_bases)

    # Eve re-encodes
    attacked_qubits = list(zip(eve_bits, eve_bases))

    return attacked_qubits
