# AfdxGetTokenData

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length, byte buffer[] ); // form 1
```

## Description

This function copies a number of bytes from a token's data area to a destination buffer.

## Return Values

number of copied bytes or 0
With AfdxGetLastError you can check if the function has been processed successfully.

## Example

Node System - preStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  AfdxRegisterReceiveCallback ( "OnAfdxPacket");
}
void OnAfdxPacket( long dir, long line, int64 timestamp, long bag, long afdxFlags, long packet )
{
  byte data[8];
  char error[100];

  // get first 8 byte (FS) of payload of the receive packet
  AfdxGetTokenData( packet, "afdx", "data", 0, 8, data );
  if (AfdxGetLastError() == 0)
  {
    // do something with data
  }
  else
  {
    AfdxGetLastErrorText( elCount(error), error );
    write("Error: %s", error );
  }
}
```

## Availability

| Since Version |
|---|
