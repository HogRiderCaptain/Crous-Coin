
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

## Blockchain Structure in the Simulation

In the Mid£Coin simulation, the blockchain is represented as a series of blocks, each containing a set of transactions, the previous block's hash (Prev Code), a proof of work, and the new block's hash. Here's an example of how the blockchain looks in the simulation:

```
+----------------------------------------------------------------------------+
Prev Code: 0000000000000000000000000000000000000000000000000000000000000000 

Transactions : 
Tx num 0 : Mugsy99 envoi 90.28MC à Sergio.
Tx num 1 : Mugsy99 envoi 4.06MC à Brand.
Tx num 2 : Mugsy99 envoi 3.02MC à Sergio.
Tx num 3 : Brand envoi 27.85MC à Levy.
Tx num 4 : Goat envoi 24.06MC à Mugsy99.
Proof of Work: 2377073
Hash block: 0000081f1ef6ad08705d7c4fcd090fb4b266487be2ab9cdcda713ccd693fc368
+----------------------------------------------------------------------------+
                          ||| 
                          VVV
+----------------------------------------------------------------------------+
Prev Code: 0000081f1ef6ad08705d7c4fcd090fb4b266487be2ab9cdcda713ccd693fc368 

Transactions : 
Tx num 5 : Mugsy99 envoi 17.98MC à Sergio.
Tx num 6 : Levy envoi 35.04MC à Mugsy99.
Tx num 7 : Brand envoi 98.38MC à Goat.
Tx num 8 : Mugsy99 envoi 36.12MC à Levy.
Tx num 9 : Goat envoi 3.93MC à Sergio.
Proof of Work: 19714
Hash block: 00000e1f1b0bb523e70e36dbc42b244dbfd6116fa7cfc26e1187b6d4be433816
+----------------------------------------------------------------------------+
                          ||| 
                          VVV
+----------------------------------------------------------------------------+
Prev Code: 00000e1f1b0bb523e70e36dbc42b244dbfd6116fa7cfc26e1187b6d4be433816 

Transactions : 
Tx num 10 : Brand envoi 67.72MC à Goat.
Tx num 11 : Brand envoi 5.51MC à Mugsy99.
Tx num 12 : Sergio envoi 101.44MC à Brand.
Tx num 13 : Goat envoi 79.99MC à Sergio.
Tx num 14 : Goat envoi 49.23MC à Mugsy99.
Proof of Work: 268298
Hash block: 00000857d60cbd0b446718dc1bb84be518b1155d0a88d8544facd0689558011d
+----------------------------------------------------------------------------+
                          ||| 
                          VVV
+----------------------------------------------------------------------------+
Prev Code: 00000857d60cbd0b446718dc1bb84be518b1155d0a88d8544facd0689558011d 

Transactions : 
Tx num 15 : Levy envoi 56.48MC à Mugsy99.
Tx num 16 : Goat envoi 40.77MC à Mugsy99.
Tx num 17 : Goat envoi 106.22MC à Sergio.
Tx num 18 : Levy envoi 3.91MC à Sergio.
Tx num 19 : Brand envoi 75.38MC à Levy.
Proof of Work: 167208
Hash block: 00000848e717da8c2fcce7c5ccf7397aeffdf366de1df9a82219d614dbce00fa
+----------------------------------------------------------------------------+

Balances:
- Brand possède 80.66MC
- Sergio possède 303.89MC
- Mugsy99 possède 159.63MC
- Levy possède 143.92MC
- Goat possède 11.9MC
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


