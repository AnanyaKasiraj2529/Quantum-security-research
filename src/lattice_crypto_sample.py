# lattice_crypto.py

import numpy as np


def generate_keys(n=4, q=97):
    A = np.random.randint(0, q, (n, n))
    s = np.random.randint(0, q, n)
    return A, s


def sample_error(n):
    return np.random.normal(0, 1, n).astype(int)


def encrypt(m, A, s, q=97):
    e = sample_error(len(s))
    c = (np.dot(A, m) + e) % q
    return c


def decrypt(c, A, s, q=97):
    # Simplified decryption
    A_inv = np.linalg.pinv(A)
    m = np.round(np.dot(A_inv, c)) % q
    return m.astype(int)
