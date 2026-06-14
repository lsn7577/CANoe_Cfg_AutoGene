# EthSetTokenData

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, char data[] );
```

## Description

The function sets the data or a part of data of a token.

It does not resize the token. Use EthResizeToken to change the length.

## Example

```c
see example of EthInitPacket
```

## Availability

| Up to Version |
|---|
