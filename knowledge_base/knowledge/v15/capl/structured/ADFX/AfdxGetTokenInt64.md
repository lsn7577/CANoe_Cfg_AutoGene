# AfdxGetTokenInt64

> Category: `ADFX` | Type: `function`

## Syntax

```c
int64 AfdxGetTokenInt64( long packet, char protocolDesignator[], char tokenDesignator[] ); // form 1
int64 AfdxGetTokenInt64( long packet, char protocolDesignatorl[], char tokenDesignator[], long offset, long length, long networkByteOrder ); // form 2
```

## Description

This function returns the specified token's data as an 64-bit integer value. With additional parameters (form 2) the user may specify the starting byte, length and byte ordering of the extracted integer value.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket. |
| protocolDesignator | Name of the protocol, e.g. "afdx". |
| tokenDesignator | Name of the token, e.g. "lpvSpeed". |
| offset | This is the offset from the beginning of the token's data area. If this is 0, data is copied starting at byte 0 of the token's data area. |
| length | This is the length of the integer value to be returned from the token's data (range 1..8). |
| networkByteOrder | 0: INTEL (little-endian) 1: MOTOROLA (big-endian) |

## Return Values

Integer value gathered from the token's data.
With AfdxGetLastError you have to check if the function has been processed successfully.

## Example

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
