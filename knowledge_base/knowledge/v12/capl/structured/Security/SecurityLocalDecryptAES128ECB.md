# SecurityLocalDecryptAES128ECB

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalDecryptAES128ECB(byte key[], dword keyLength, byte cipheredData[], dword cipheredDataLength, byte plainData[], dword plainDataLength)
```

## Description

Decrypts ciphered data with a given key using AES128 (ECB), Padding Mode PKCS5.

## Return Values

1: Success. A Value of 1 means that the action was successful.

## Availability

| Since Version |
|---|
