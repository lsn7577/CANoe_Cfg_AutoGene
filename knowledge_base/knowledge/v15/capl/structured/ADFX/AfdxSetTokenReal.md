# AfdxSetTokenReal

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetTokenReal( long packet, char protocolDesignator[], char tokenDesignator[], long offset, long length, float value );
```

## Description

This function sets the specified token‘s data as a float value.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket. |
| protocolDesignator | Name of the protocol, e.g. "udp". |
| tokenDesignator | Name of the token, e.g. "data". |
| offset | This is the offset from the beginning of the token's data area. If this is 0, data is copied starting at byte 0 of the token's data area. |
| length | The values 4 (32-bit float value) and 8 (64-bit float value) are allowed here. This is the length of the value to be copied to the token's data area. |
| value | New value. |

## Example

```c
{
  // have  a packet handle <packet> created already
  long err = 0;
  err = AfdxSetTokenReal( packet, "udp", "data", 8, 8, 1.234);
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
