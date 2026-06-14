# EthGetTokenLengthBit

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetTokenLengthBit( long packet, char protocolDesignator[], char tokenDesignator[] );
```

## Description

The function returns the length of a token in bit.

## Return Values

length of the token in bit
With EthGetLastError you can check if the function has been processed successfully.

## Example

```c
LONG packet = 0;
LONG len = 0;
CHAR error[100];

packet = EthInitPacket( "udp" );
len    = EthGetTokenLengthBit( packet, "udp", "source" ); // = 32

if (EthGetLastError() == 0)
{
  // do something with len
}
else
{
  EthGetLastErrorText( elCount(error), error );
  write("Error: %s", error );
}
```

## Availability

| Up to Version |
|---|
