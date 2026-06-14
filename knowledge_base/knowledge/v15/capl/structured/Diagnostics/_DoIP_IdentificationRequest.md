# _DoIP_IdentificationRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long _DoIP_IdentificationRequest(long type, BYTE VINorEID[]);
```

## Description

A vehicle simulation has received a Vehicle Identification Request Message. The value returned will determine the reaction of the DoIP.DLL.

Note that requests not targeted at the ECU will be ignored.

## Parameters

| Name | Description |
|---|---|
| type | 1: No argument, VINorEID is empty2: Argument contains the EID (6 byte)3: Argument contains the VIN (17 byte/characters) |
| VINorEID | The argument from the request message. |

## Example

```c
long _DoIP_IdentificationRequest(long type, BYTE VINorEID[])
{
  if( type == 1)
    write( "Received VIR without argument");
  else if( type == 2)
    write( "Received VIR with EID: %02x:%02x:%02x:%02x:%02x:%02x"
    , VINorEID[0], VINorEID[1], VINorEID[2]
    , VINorEID[3], VINorEID[4], VINorEID[5]);
  else if( type == 3)
  {
    char textVIN[17];
    int i;
    for( i = 0; i < elcount(VINorEID); ++i)
      textVIN[i] = VINorEID[i];
    write( "Received VIR with VIN: %s", textVIN);
  }
  // The response message shall be sent after waiting between 100 and 500 ms
  return 100 + random(400);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP4 | — | — | — | 1.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
