# AfdxGetTokenLengthBit

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetTokenLengthBit( long packet, char protocolDesignator[], char tokenDesignator[] );
```

## Description

This function returns the length of a token in bit.

## Return Values

length of the token in bit
With AfdxGetLastError you have to check if the function has been processed successfully.

## Example

```c
long packet = 0;
long len = 0;
char error[100];

packet = AfdxInitPacket( "afdx" );
len = AfdxGetTokenLengthBit( packet, "afdx", "data" );
if (AfdxGetLastError() == 0)
{
  // do something with len
}
else
{
  AfdxGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
```

## Availability

| Since Version |
|---|
