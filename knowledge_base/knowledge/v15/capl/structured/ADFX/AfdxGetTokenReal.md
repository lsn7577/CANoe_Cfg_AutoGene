# AfdxGetTokenReal

> Category: `ADFX` | Type: `function`

## Syntax

```c
float AfdxGetTokenReal( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length );
```

## Description

This function returns the specified token's data as a float value.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket or from within a callback. |
| protocolDesignator | Name of the protocol, e.g. "udp". |
| tokenDesignator | Name of the token, e.g. "data". |
| offset | This is the offset from the beginning of the token's data area. If this is 0, data is copied starting at byte 0 of the token's data area. |
| length | The values 4 (32-bit float value) and 8 (64-bit float value) are allowed here. This is the length of the value to be returned from the token's data area. |

## Return Values

Integer value gathered from the token's data.
With AfdxGetLastError you have to check if the function has been processed successfully.

## Example

```c
void OnAfdxPacket(long channel, long dir, long flags, long bag, long packet )
{
  double temperature;
  char error[100];

  // get temperature value from payload position 8 as a float (4byte length)
  temperature = AfdxGetTokenReal( packet, "udp", "data", 8, 4 );

  if (AfdxGetLastError() == 0)
  {
    // do something with temperature
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
| Since Version | — | 8.0 SP2 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
