# C2xGetTokenData

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long length, char buffer[] );
```

## Description

This function requests the data or a part of date of a token.

## Return Values

Number of copied bytes or 0
With C2xGetLastError you can check if the function has been processed successfully.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  C2xReceivePacket( "OnC2xPacket" );
}
void OnC2xPacket( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  byte data[5];
  char error[100];

  // get payload of the receive packet
  C2xGetTokenData( packet, "geo_cnh", "data", 5, data );
  if (C2xGetLastError() == 0)
  {
    // do something with data
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
