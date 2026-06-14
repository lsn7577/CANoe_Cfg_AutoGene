# AfdxGetTokenInt

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetTokenInt( long packet, char protocolDesignator[], char tokenDesignator[] ); // form 1
```

## Description

This function returns the specified token‘s data as an integer value. With additional parameters (form 2) the user may specify the starting byte, length and byte ordering of the extracted integer value.

Note: The network byte order interpretation for form 1 is big-endian.

## Return Values

integer value gathered from the token's data
With AfdxGetLastError you have to check if the function has been processed successfully.

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
  long status;
  char error[100];

  // get status byte 1  of FDS1 (offset=4, length=1byte)
  status = AfdxGetTokenInt( packet, "udp", "data", 4, 1, 1 );
  if (AfdxGetLastError() == 0)
  {
    // do something with status
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
