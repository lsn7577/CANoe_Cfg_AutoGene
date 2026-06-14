# EthGetTokenSubString

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetTokenSubString( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, char buffer[] );
```

## Description

The function copies a specified number of characters from a given position inside the token and adds a terminating "\0".

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
  EthGetTokenSubString( packetHandle, "ipv4", "data", 8, elCount(rx_str), rx_str );
  // would access payload of an udp packet

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
