# AfdxSetTokenData

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length, byte buffer[] ); // form 1
```

## Description

This function copies a number of bytes from source buffer to a token's data area. The token is not resized. Use AfdxResizeToken to change the token's length.

## Availability

| Since Version |
|---|
