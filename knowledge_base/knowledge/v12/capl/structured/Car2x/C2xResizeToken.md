# C2xResizeToken

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xResizeToken( long packet, char protocolDesignator[], char tokenDesignator[], long newBitLength );
```

## Description

This function sets the length of a token.

In case the token length is increased by full bytes, the additional bytes are initialized with 0.

## Return Values

0 or error code

## Availability

| Since Version |
|---|
