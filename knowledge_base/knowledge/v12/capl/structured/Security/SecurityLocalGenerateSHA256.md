# SecurityLocalGenerateSHA256

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalGenerateSHA256(byte data[], dword dataLength, byte sha256[], dword sha256Length)
```

## Description

Generates a SHA256 hash for the given data and key. The generated hash is a SipHash.

## Return Values

1: SuccessA Value of 1 means that the action was successful.

## Availability

| Since Version |
|---|
