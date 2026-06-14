# EthGetTokenInt

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetTokenInt( long packet, char protocolDesignator[], char tokenDesignator[] ); // form 1
```

## Description

The function requests the integer value of a token.

Form 2 with byte offset returns a part of the token data as integer.

## Return Values

integer value of the token or 0
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
  LONG destPort;
  CHAR error[100];

  // get destination port of the receive packet
  destPort = EthGetTokenInt( packetHandle, "udp", "destination" );

  if (EthGetLastError() == 0)
  {
    // do something with destPort
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
