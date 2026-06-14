# C2xGetTokenLengthBit

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetTokenLengthBit( long packet, char protocolDesignator[], char tokenDesignator[] );
```

## Description

This function returns the length of a token in bit.

## Return Values

Length of the token in bit
With C2xGetLastError you can check if the function has been processed successfully.

## Example

```c
long packet = 0;
long len = 0;
char error[100];

packet = C2xInitPacket( "geo_cnh" );
len    = C2xGetTokenLengthBit( packet, "geo_cnh", "header" ); // = 32

if (C2xGetLastError() == 0)
{
  // do something with len
}
else
{
  C2xGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
```

## Availability

| Since Version |
|---|
