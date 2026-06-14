# EthGetTokenString

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetTokenString( long packet, char protocolDesignator[], char tokenDesignator[], long bufferSize, char buffer[] );
```

## Description

The function copies characters from the token and adds a terminating "\0".

## Return Values

number of copied characters or 0
With EthGetLastError you can check if the function has been processed successfully.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  EthReceivePacket("OnEthPacket");
}
void OnEthPacket( LONG channel, LONG dir, LONG packetHandle )
{
  CHAR rx_str[100];
  CHAR error[100];

  // get the payload of the packet
  EthGetTokenString( packetHandle, "udp", "data", elCount(rx_str), rx_str );

  if (EthGetLastError() == 0)
  {
    write(rx_str);
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
