# AfdxGetTokenString

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetTokenString( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long bufSize, char buffer[] );
```

## Description

This function copies characters from the token and adds a terminating "\0".

## Return Values

number of copied characters or 0
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
  char rx_str[100];
  char error[100];

  // get a string value located in FDS1
  long offset = 8; // FDS1 + 2 byte length info
  long status  = 0;
  long len = 0;

  len = AfdxGetTokenInt( packet, "udp", "data", offset, 2, 1 );

  if (AfdxGetLastError() == 0)
  {
    AfdxGetTokenString( packet, "udp", "data", offset+2,  len, rx_str );
    if (AfdxGetLastError() == 0)
    {
      write(rx_str);
    }
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
