# AfdxGetTokenData

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length, byte buffer[] ); // form 1
long AfdxGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length, char buffer[] ); // form 2
long AfdxGetTokenData( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length, struct * buffer ); // form 3
```

## Description

This function copies a number of bytes from a token's data area to a destination buffer.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket. |
| protocolDesignator | Name of the protocol, e.g. "afdx". |
| tokenDesignator | Name of the token, e.g. "data". |
| offset | This is the offset from the beginning of the token's data area. If this is 0, data is copied starting at byte 0 of the token's data area. |
| length | This is the number of bytes to be copied from the token's data area to the specified buffer. |
| buffer | This is the destination buffer for the copied data. Make sure that the size of the buffer is at least length bytes. |

## Return Values

number of copied bytes or 0
With AfdxGetLastError you can check if the function has been processed successfully.

## Example

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2, 3 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
