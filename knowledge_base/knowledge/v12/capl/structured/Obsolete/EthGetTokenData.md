# EthGetTokenData

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, char buffer[] );
```

## Description

The function requests the data or a part of date of a token.

## Return Values

number of copied bytes or 0
With EthGetLastError you can check if the function has been processed successfully.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  EthReceivePacket( "OnEthPacket" );
}
void OnEthPacket( LONG channel, LONG dir, LONG packetHandle )
{
  BYTE data[5];
  CHAR error[100];

  // get udp payload of the receive packet
  EthGetTokenData( packetHandle, "udp", "data", 5, data );
  if (EthGetLastError() == 0)
  {
    // do something with data
  }
  else
  {
    EthGetLastErrorText( elCount(error), error );
    write("Error: %s", error );
  }
}
```

## Availability

| Up to Version |
|---|
