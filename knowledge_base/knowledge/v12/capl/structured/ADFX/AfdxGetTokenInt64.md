# AfdxGetTokenInt64

> Category: `ADFX` | Type: `function`

## Syntax

```c
int64 AfdxGetTokenInt64( long packet, char protocolDesignator[], char tokenDesignator[] ); // form 1
```

## Description

This function returns the specified token's data as an 64-bit integer value. With additional parameters (form 2) the user may specify the starting byte, length and byte ordering of the extracted integer value.

Note: The network byte order interpretation for form 1 is big-endian.

## Return Values

integer value gathered from the token's data
With AfdxGetLastError you have to check if the function has been processed successfully.

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  AfdxRegisterReceiveCallback ( "OnAfdxPacket");
}
void OnAfdxPacket( long dir, long line, int64 timestamp, long bag, long afdxFlags, long packet )
{
  int64 timeTS;
  char error[100];

  // get a signed double length integer at FDS1 (offset = 8) with length 8:
  timeTS = AfdxGetTokenInt64(packet, "afdx", "data", 8, 8, 1 );
  if (AfdxGetLastError() == 0)
  {
    // do something with timeTS
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
