# LocalSecurityGenerateSharedSecretECDH

> Category: `Obsolete` | Type: `notes`

## Description

Replaced by SecurityLocalGenerateSharedSecretECDH.

| Deprecated Function Replaced by SecurityLocalGenerateSharedSecretECDH. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long LocalSecurityGenerateSharedSecretECDH(BYTE[] publicKey, dword publicKeyLength, BYTE[] privateKey, dword privateKeyLength, BYTE[] sharedSecret, dword sharedSecretLength) |  |  |  |
| Function | Generates a shared Secret between A and B for a given public key of A and private Key and B. The Elliptic Curve Diffie-Hellman (ECDH)protocol (X25519) is used. |  |  |  |
| Parameters | publicKey The public key of A |  |  |  |
| publicKeyLength 32 bytes |  |  |  |  |
| privateKey The private key of B |  |  |  |  |
| privateKeyLength 32 bytes |  |  |  |  |
| output The generated shared secret |  |  |  |  |
| outputLength 32 bytes |  |  |  |  |
| Return Values | Successful = 1, Failed <= 0 |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 11.0 SP2 | - | — | • |  |

| Version 15© Vector Informatik GmbH |
|---|
