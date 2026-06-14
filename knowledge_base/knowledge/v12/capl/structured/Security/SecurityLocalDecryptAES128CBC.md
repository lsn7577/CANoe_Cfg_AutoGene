# SecurityLocalDecryptAES128CBC

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalDecryptAES128CBC(byte key[], dword keyLength, byte cipheredData[], dword cipheredDataLength, byte initVector[], dword initVectorLength, byte plainData[], dword plainDataLength)
```

## Description

Decrypts ciphered data with a given key and initialization vector using AES128 (CBC), Padding Mode PKCS5.

## Return Values

1: Success. A Value of 1 means that the action was successful.

## Availability

| Since Version |
|---|
