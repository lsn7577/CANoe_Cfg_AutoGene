# AfdxGetTokenString

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetTokenString( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long bufSize, char buffer[] );
```

## Description

This function copies characters from the token and adds a terminating "\0".

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket. |
| protocolDesignator | Name of the protocol, e.g. "afdx". |
| tokenDesignator | Name of the token, e.g. "data". |
| offset | This is the offset from the beginning of the token's data area. If this is 0, data is copied starting at byte 0 of the token's data area. |
| bufSize | Size of buffer in bytes. This function adds a terminating "\0". Thus the maximum number of copied characters is length-1. |
| buffer | The characters are copied to this buffer area. |

## Return Values

Number of copied characters or 0.
With AfdxGetLastError you have to check if the function has been processed successfully.

## Example

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
