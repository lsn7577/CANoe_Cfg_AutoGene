# AfdxSetTokenInt64

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetTokenInt64( long packet, char protocolDesignator[], char tokenDesignator[], int64 value ); // form 1
```

## Description

This function sets the specified token‘s data to a new 64-bit integer value. With additional parameters (form 2) the user may specify the starting byte, length and byte ordering of the integer value in the token.

Note: The network byte order interpretation for form 1 is big-endian.

## Return Values

0 or error code

## Availability

| Since Version |
|---|
