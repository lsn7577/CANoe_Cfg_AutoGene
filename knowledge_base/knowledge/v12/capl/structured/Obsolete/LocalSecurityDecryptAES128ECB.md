# LocalSecurityDecryptAES128ECB

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long LocalSecurityDecryptAES128ECB(BYTE[] key, dword keyLength, BYTE[] cipheredData, dword cipheredData Length, BYTE[] plainData, dword plainData Length)
```

## Description

Decrypts data with a given key and initialization vector. The decryption is AES128 (ECB), PKCS5 Padding.

## Availability

| Up to Version |
|---|
