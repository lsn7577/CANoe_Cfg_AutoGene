# SecurityLocalGenerateSharedSecretECDH

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalGenerateSharedSecretECDH(byte publicKey[], dword publicKeyLength, byte privateKey[], dword privateKeyLength, byte sharedSecret[], dword* sharedSecretLength)
```

## Description

Generates a shared Secret between A and B for a given public key of A and private Key of B. The Elliptic Curve Diffie-Hellman (ECDH) protocol (X25519) is used.

## Return Values

1: SuccessA Value of 1 means that the action was successful.

## Availability

| Since Version |
|---|
