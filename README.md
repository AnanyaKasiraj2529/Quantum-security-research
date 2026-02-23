🔐 Quantum-Safe Hybrid Key Distribution for IoT
BB84 Quantum Key Distribution + Lattice-Based Post-Quantum Authentication
📌 Project Overview

This repository presents a hybrid quantum-safe communication framework that integrates:

BB84 Quantum Key Distribution (QKD)

Lattice-Based Post-Quantum Cryptography (PQC)

Hybrid QKD + PQC Authentication Model

Quantum Bit Error Rate (QBER) Analysis

Eavesdropper (Eve) Attack Simulation

The goal is to design and simulate a quantum-resilient key exchange protocol suitable for resource-constrained IoT environments, addressing scalability, side-channel risks, and future quantum threats.

This implementation supports the research work presented in:

Quantum-Safe Protocols Design for IoT Communications: Critical Observation and Analysis (CISCON 2025)

🧠 Motivation

With the rise of quantum computing:

Classical cryptographic schemes (RSA, ECC) are vulnerable to Shor’s Algorithm

IoT systems operate under low power and limited computation

Pure QKD systems suffer from scalability and noise sensitivity

Lattice-based cryptography faces side-channel vulnerabilities

This project explores a hybrid security architecture combining the strengths of both paradigms.

🏗 Repository Structure
Quantum-Safe-BB84-Lattice-Hybrid/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── paper/
│   └── CISCON_2025_Camera_Ready.pdf
│
├── notebooks/
│   ├── 1_Comparative_study_of_QKD_algorithms.ipynb
│   ├── 2_QKD_and_PQKD_Simulations.ipynb
│
├── src/
│   ├── bb84.py
│   ├── lattice_crypto.py
│   ├── hybrid_protocol.py
│   ├── qber.py
│   └── attack_models.py
│
│
└── images/
🔬 Implementation architecture design
1️⃣ BB84 Quantum Key Distribution

Simulates:

Random bit generation

Random basis selection (Z / X)

Measurement process

Key sifting

Secure shared key formation

📓 Notebook: 1_BB84_Simulation.ipynb

2️⃣ Lattice-Based Encryption (LWE-Inspired)

Implements:

Public matrix generation

Error sampling

Encryption:

c = A·m + e mod q

Decryption via approximate inversion

📓 Notebook: 2_Lattice_Based_Encryption.ipynb

3️⃣ Hybrid QKD + PQC Model

Workflow:

Generate QKD shared key

Apply lattice-based authentication

Perform layered encryption

Evaluate correctness

📓 Notebook: 3_Hybrid_QKD_PQC_Model.ipynb

4️⃣ QBER & Attack Analysis

Simulates:

Intercept-resend Eve attack

Error introduction in quantum channel

QBER comparison (clean vs attacked channel)

Expected Results:

Scenario	QBER
No Attack	≈ 0
With Attack	20–30%

📓 Notebook: 4_QBER_and_Attack_Analysis.ipynb

📊 Key Experimental Results

✔ ~50% key retention in BB84
✔ Successful lattice encryption & decryption
✔ Detectable QBER increase under attack
✔ Demonstration of hybrid quantum-safe layering

🛡 Security Insights

This hybrid approach:

Provides quantum-safe key exchange

Adds post-quantum authentication

Improves resilience against:

Quantum computing attacks

Side-channel threats

Eavesdropping attempts

Supports scalability research for IoT systems

🚀 How to Run
1️⃣ Clone Repository
git clone https://github.com/yourusername/Quantum-Safe-BB84-Lattice-Hybrid.git
cd Quantum-Safe-BB84-Lattice-Hybrid
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Notebooks
jupyter notebook

Open notebooks in sequence:

1 → 2 → 3 → 4

🔮 Future Research Directions

Integration with Cirq or Qiskit quantum circuits

RLWE-based cryptographic expansion

AI-based side-channel detection

Error correction (Steane Code)

IoT computational benchmarking

Hybrid protocol latency optimization

📚 Research Contribution

This repository bridges:

Quantum cryptography

Post-quantum cryptography

Hybrid secure protocol design

IoT security architecture

It serves as:

Research support material

Simulation framework

Educational reference

Foundation for quantum-safe protocol experimentation

📜 Citation

If you use this work, please cite:

Kasiraj et al.,
Quantum-Safe Protocols Design for IoT Communications:
Critical Observation and Analysis,
CISCON 2025.
👩‍💻 Author

Ananya Kasiraj
Cybersecurity Researcher
Quantum-Safe Cryptography | IoT Security | Post-Quantum Systems

⭐ Why This Repository Matters

As quantum computing advances, future communication systems must:

Resist quantum cryptanalysis

Operate under IoT constraints

Detect eavesdropping in real time

Balance scalability and security

This project demonstrates a practical research-backed hybrid solution.
