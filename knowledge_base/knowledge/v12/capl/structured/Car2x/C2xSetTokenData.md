# C2xSetTokenData

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, char data[] );
```

## Description

This function sets the data or a part of data of a token.

It does not resize the token. Use C2xResizeToken to change the length.

## Return Values

0 or error code

## Availability

| Since Version |
|---|
