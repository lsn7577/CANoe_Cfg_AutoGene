# GNSSSetPosDataVal

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetPosDataVal(dword fixSID, dword systemAndMethod, dword integrity, dword numOfSVs, dword hdop, dword pdop, dword geoSeparation, dword numOfRefStat, dword refStations[]}
```

## Description

This function can be used to change values of parameter group "GNSS Position Data" (PGN 129029) which are not modified by the simulation automatically.

## Parameters

| Name | Description |
|---|---|
| fixSID | 1 if fix sequence ID (255) has to be used, else 0 |
| systemAndMethod | the first 4 bit specifies the system type, the upper 4 bit the GNSS Method |
| integrity | integrity |
| numOfSVs | number of visible satellites |
| hdop | horizontal dilution of precision |
| pdop | position dilution of precision |
| geoSeparation | geoidal separation |
| numOfRefStat | number of reference stations |
| refStations | array of reference stations, every station is specified by 4 bytes (Bit 0-3: Type, Bit 4-15: ID, Bit 16-31: Ages of DGNSS Corrections) |

## Return Values

error code

## Example

```c
dword refSta[2];
refStation[0] = 0x11110010;
refStation[1] = 0x22220020;
GNSSSetPosDataVal(0,0x20,1,4,21,54,763,2,refSta);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | — |
| Restricted To | — | J1939 ISO11783 | J1939 ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
