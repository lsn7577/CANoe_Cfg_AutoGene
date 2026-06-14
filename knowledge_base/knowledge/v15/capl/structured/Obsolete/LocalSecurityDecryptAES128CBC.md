# LocalSecurityDecryptAES128CBC

> Category: `Obsolete` | Type: `notes`

## Description

Replaced by SecurityLocalDecryptAES128CBC

| Deprecated Function Replaced by SecurityLocalDecryptAES128CBC |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long LocalSecurityDecryptAES128CBC(BYTE[] key, dword keyLength, BYTE[] cipheredData, dword cipheredData Length, BYTE[] initVector, dword initVectorLength, BYTE[] plainData, dword plainData Length) |  |  |  |
| Function | Decrypts data with a given key and initialization vector. The decryption is AES128 (CBC), PKCS5 Padding. |  |  |  |
| Parameters | key The key to be used for AES (128 bit) |  |  |  |
| keyLength 16 (bytes) |  |  |  |  |
| cipheredData The ciphered data to decrypt |  |  |  |  |
| cipheredDataLength The length of the ciphered data |  |  |  |  |
| initVector The init vector to be used |  |  |  |  |
| initVectorLength 16 (bytes) |  |  |  |  |
| cipheredData The buffer in which the plain data is stored. |  |  |  |  |
| cipheredDataLength The length of the buffer. Typically this buffer should have the same length as the ciphered data buffer. |  |  |  |  |
| Return Values | Successful = 1, Failed <= 0 |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 11.0 SP2 | — | — | • |  |

| Version 15© Vector Informatik GmbH |
|---|
