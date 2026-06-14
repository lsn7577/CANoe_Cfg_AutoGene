# J1939GetNumOfDTCs

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939GetNumOfDTCs(pg pgWithDTCs, dword spn, byte fmi, byte oc)
```

## Description

Function looks through a J1939 diagnostic message and returns the number of DTC blocks that match the search criteria, i.e. that contains defined SPN/FMI/OC values.

## Parameters

| Name | Description |
|---|---|
| pgWithDTC | Message to be checked for a specific DTC block. Must be a J1939 Parameter Group. |
| spn | Suspect Parameter Number of the specified DTC. 0xFFFFFFFF if spn is to be ignored. |
| fmi | Failure Mode Identifier of the specified DTC. 0xFFFF if fmi is to be ignored. |
| oc | Occurrence Counter of the specified DTC . 0xFFFF if oc is to be ignored. |

## Example

```c
on pg DM1
{
  int numOfDTCs;

  //Count the number of DTCs with FMI=11
  numOfDTCs = J1939GetNumOfDTCs (this, 0xFFFFFFFF, 11, 0xFFFF);
  if(numOfDTCs > 0)
    WriteEx(-3, 3, "DM1 wiht %d DTC(s) with FMI=11 observed", numOfDTCs);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | J1939 | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
