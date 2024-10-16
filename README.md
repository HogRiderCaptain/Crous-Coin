
# Blockchain Simulation Project

This project simulates a blockchain environment in Python. The simulation includes key elements such as block creation, mining operations, and cryptographic processes like hashing and digital signatures. This implementation is intended for educational purposes to illustrate the mechanics behind blockchain technology.

## Report Summary

This project, *Mid£Coin*, was developed by Ali, Brandon, Sergio, and Youssef in December 2023. It explores the principles of blockchain and cryptocurrency through practical implementation in Python. The project combines cryptographic techniques, such as elliptical curve cryptography and hashing, to ensure secure transactions.

The full report can be found [here](MC_officiel.pdf).

## Mining Process Visualization

During the simulation, multiple miners equipped with different GPUs attempt to mine a block by solving the proof of work puzzle. Below is a screenshot illustrating the process:


### Example Output

```bash
Mineur Rtx4080 travaille dur ...
Mineur Rtx4060 travaille dur ...
...
Block 00000bddaf041a011970df5f0f1ec3cdfafca4d841ee76ff6d013bbdbf9fbffd
----------------------------------------------------------
Mineur Rtx4070 a été le plus performant, Levy remporte 50MC
```

## Features

- **Blockchain.py**: Handles the creation and validation of blocks in the blockchain.
- **FieldElement.py**: Provides the implementation of field elements used in elliptic curve cryptography.
- **Hash_256bits.py**: Implements the 256-bit hash function, crucial for the integrity of blocks.
- **Mineurs.py**: Simulates the behavior of miners, including the proof of work and block mining process.
- **Personne.py**: Represents participants in the blockchain, such as miners or other actors.
- **Point.py**: Contains the implementation of points on elliptic curves for cryptographic operations.
- **S256.py**: Implements specific functions for Secp256k1, a widely used elliptic curve in blockchain applications.
- **PrivateKey.py**: Manages the generation and use of private keys for signing transactions.
- **Signature.py**: Handles the creation and verification of digital signatures to secure blockchain transactions.
- **Simulation.py**: Coordinates the overall blockchain simulation, bringing together all elements to demonstrate a functional blockchain environment.

## Report Highlights

### Signature

The project focuses on ensuring that transactions are signed and verified using elliptical curve cryptography. This ensures that only the owner of the private key can sign a message (or transaction), and everyone can verify the authenticity using the public key.

### Blockchain

Each block contains:
- **Transactions**: A set of 5 transactions per block.
- **Proof of Work**: The computational effort required to add a block to the blockchain.
- **Previous Code**: The hash of the previous block to ensure chain integrity.

The blockchain uses a Proof of Work mechanism where miners compete to find a solution that satisfies a specific condition for the block's hash. This ensures security and prevents tampering.

### Simulation

The simulation involves five entities, each possessing miners. These miners compete to solve the Proof of Work, and upon success, they are rewarded in *Mid£Coin*. To control the currency supply, a halving mechanism is implemented, reducing the reward every 10 blocks.

## Getting Started

### Prerequisites

You need to have Python 3.x installed on your system to run this project. The following libraries may also be required:
- `hashlib` (for hashing functions)
- `ecdsa` (for elliptic curve digital signatures)
- `secrets` (for cryptographic randomness)
- `time` (for simulating mining delays)

You can install any missing libraries using `pip`:
```bash
pip install hashlib ecdsa
```

### Running the Simulation

1. Clone this repository:
    ```bash
    git clone https://github.com/HogRiderCaptain/Crous-Coin.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Crous-Coin
    ```
3. Run the main simulation script:
    ```bash
    python simulation.py
    ```

## Future Improvements

- Implement transaction pools for handling multiple simultaneous transactions.
- Improve the mining algorithm to better reflect real-world difficulty adjustment.
- Add a GUI to visualize the blockchain and mining operations.
- Introduce smart contracts and more complex transaction types.


