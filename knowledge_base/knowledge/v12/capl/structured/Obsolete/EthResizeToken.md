# EthResizeToken

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthResizeToken( long packet, char protocolDesignator[], char tokenDesignator[], long newBitLength );
```

## Description

The function sets the length of a token.

In case the token length is increased by full bytes, the additional bytes are initialized with 0.

## Return Values

0 or error code

## Example

```c
see example of EthInitPacket
```

## Availability

| Up to Version |
|---|
