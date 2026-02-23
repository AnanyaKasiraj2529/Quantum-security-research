# bb84.py

import numpy as np


def generate_bits(n):
    return np.random.randint(0, 2, n)


def generate_bases(n):
    return np.random.randint(0, 2, n)  # 0 = Z basis, 1 = X basis


def encode_qubits(bits, bases):
    # In simulation, qubits are just stored as (bit, basis)
    return list(zip(bits, bases))


def measure_qubits(qubits, measurement_bases):
    measured_bits = []

    for i, (bit, basis) in enumerate(qubits):
        if basis == measurement_bases[i]:
            measured_bits.append(bit)  # Correct measurement
        else:
            measured_bits.append(np.random.randint(0, 2))  # Random if wrong basis

    return np.array(measured_bits)


def sift_key(alice_bits, alice_bases, bob_bits, bob_bases):
    key = []
    for i in range(len(alice_bits)):
        if alice_bases[i] == bob_bases[i]:
            key.append(alice_bits[i])
    return np.array(key)


def run_bb84(n=100):
    alice_bits = generate_bits(n)
    alice_bases = generate_bases(n)

    qubits = encode_qubits(alice_bits, alice_bases)

    bob_bases = generate_bases(n)
    bob_bits = measure_qubits(qubits, bob_bases)

    shared_key = sift_key(alice_bits, alice_bases, bob_bits, bob_bases)

    return shared_key
