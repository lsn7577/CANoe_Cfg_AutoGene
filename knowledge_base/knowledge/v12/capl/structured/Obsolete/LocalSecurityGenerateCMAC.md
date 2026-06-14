# LocalSecurityGenerateCMAC

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long LocalSecurityGenerateCMAC(BYTE[] key, dword keyLength, BYTE[] data, dword dataLength, BYTE[] output, dword outputLength)
```

## Description

Generates a hash for the given data and key. The generated Hash is a CMAC.

## Availability

| Up to Version |
|---|
