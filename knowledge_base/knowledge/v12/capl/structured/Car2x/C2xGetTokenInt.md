# C2xGetTokenInt

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetTokenInt( long packet, char protocolDesignator[], char tokenDesignator[] ); // form 1
```

## Description

This function requests the integer value of a token.

Form 2 with byte offset returns a part of the token data as integer.

## Return Values

Integer value of the token or 0
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
  long speed;
  char error[100];

  // get lpvSpeed of the receive packet
  speed = C2xGetTokenInt( packet, "geo_cnh", "lpvSpeed" );
  if (C2xGetLastError() == 0)
  {
    // do something with lpvSpeed
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
