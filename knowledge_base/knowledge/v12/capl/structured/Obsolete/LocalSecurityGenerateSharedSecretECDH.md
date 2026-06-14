# LocalSecurityGenerateSharedSecretECDH

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long LocalSecurityGenerateSharedSecretECDH(BYTE[] publicKey, dword publicKeyLength, BYTE[] privateKey, dword privateKeyLength, BYTE[] sharedSecret, dword sharedSecretLength)
```

## Description

Generates a shared Secret between A and B for a given public key of A and private Key and B. The Elliptic Curve Diffie-Hellman (ECDH)protocol (X25519) is used.

## Availability

| Up to Version |
|---|
