# C2xGetTokenSubString

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetTokenSubString( long packet, char protocolDesignator[], char tokenDesignator[], long byteOffset, long length, char buffer[] );
```

## Description

This function copies a specified number of characters from a given position inside the token and adds a terminating \0.

## Return Values

Number of copied characters or 0
With C2xGetLastError you can check if the function has been processed successfully.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  C2xReceivePacket("OnC2xPacket");
}
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  char rx_str[100];
  char error[100];

  // get the payload of the packet
  C2xGetTokenSubString( packet, "geo_cnh", "data", 8, elCount(rx_str), rx_str );
  // would access payload of a cnh packet

  if (C2xGetLastError() == 0)
  {
    write(rx_str);
  }
  else
  {
    C2xGetLastErrorText( elCount(error), error );
    write("Error: %s", error );
  }
}
```

## Availability

| Since Version |
|---|
