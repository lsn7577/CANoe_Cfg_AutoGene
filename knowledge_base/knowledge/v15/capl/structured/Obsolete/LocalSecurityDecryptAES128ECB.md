# LocalSecurityDecryptAES128ECB

> Category: `Obsolete` | Type: `notes`

## Description

Replaced by SecurityLocalDecryptAES128ECB.

| Deprecated Function Replaced by SecurityLocalDecryptAES128ECB. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long LocalSecurityDecryptAES128ECB(BYTE[] key, dword keyLength, BYTE[] cipheredData, dword cipheredData Length, BYTE[] plainData, dword plainData Length) |  |  |  |
| Function | Decrypts data with a given key and initialization vector. The decryption is AES128 (ECB), PKCS5 Padding. |  |  |  |
| Parameters | key The key to be used for AES (128 bit) |  |  |  |
| keyLength 16 (bytes) |  |  |  |  |
| cipheredData The ciphered data to decrypt |  |  |  |  |
| cipheredDataLength The length of the ciphered data |  |  |  |  |
| plainData The buffer in which the plain data is stored. |  |  |  |  |
| plainDataLength The length of the buffer. Typically this buffer should have the same length as the ciphered data buffer. |  |  |  |  |
| Return Values | Successful = 1, Failed <= 0 |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 11.0 SP2 | — | — | • |  |

| Version 15© Vector Informatik GmbH |
|---|
