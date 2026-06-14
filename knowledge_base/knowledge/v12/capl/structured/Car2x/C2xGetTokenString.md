# C2xGetTokenString

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetTokenString( long packet, char protocolDesignator[], char tokenDesignator[], long bufferSize, char buffer[] );
```

## Description

This function copies characters from the token and adds a terminating \0.

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
  C2xGetTokenString( packet, "geo_cnh", "data", elCount(rx_str), rx_str );

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
