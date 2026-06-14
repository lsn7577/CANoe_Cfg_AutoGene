# SecurityLocalGenerateSHA512

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalGenerateSHA512(byte data[], dword dataLength, byte sha512[], dword sha512Length)
```

## Description

Generates a SHA512 hash for the given data and key. The generated hash is a SipHash.

## Return Values

A Value of 1 means that the action was successful. A value less than or equal to 0 means error.

## Availability

| Since Version |
|---|
