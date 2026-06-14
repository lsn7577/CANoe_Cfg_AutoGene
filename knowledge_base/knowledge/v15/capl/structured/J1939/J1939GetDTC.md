# J1939GetDTC

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939GetDTC(pg pgWithDTC, dword spn, byte fmi, byte oc, dword &dtcValue)
```

## Description

Function looks through a J1939 diagnostic message and returns the first DTC block that matches the search criteria, i.e. that contains defined SPN/FMI/OC values.

## Parameters

| Name | Description |
|---|---|
| pgWithDTC | Message to be checked for a specific DTC block. Must be a J1939 Parameter Group. |
| spn | Suspect Parameter Number of the specified DTC. 0xFFFFFFFF if spn is to be ignored. |
| fmi | Failure Mode Identifier of the specified DTC. 0xFFFF if fmi is to be ignored. |
| oc | Occurrence Counter of the specified DTC . 0xFFFF if oc is to be ignored. |
| dtcValue | The value of the found DTC block. |

## Example

```c
on pg DM1
{
  int posOfDTC;
  dword foundDTC;
  word fmi, oc;
  dword spn;

  //Look for the DTC with SPN=67890
  posOfDTC = J1939GetDTC(this, 67890, 0xFFFF, 0xFFFF, foundDTC);
  if(posOfDTC > 0)
  {
    fmi = J1939GetFmiFromDTC(foundDTC);
    oc = J1939GetOcFromDTC(foundDTC);
    WriteEx(-3, 3, "DM1 with DTC (SPN=67890) observed: FMI=%d, OC=%d", fmi, oc);
  
}
  //Look for the DTC with SPN=123 and OC=5
  posOfDTC = J1939GetDTC(this, 123, 0xFFFF, 5, foundDTC);
  if(posOfDTC > 0)
  {
    fmi = J1939GetFmiFromDTC(foundDTC);
    WriteEx(-3, 3, "DM1 with DTC (SPN=123, OC=5) observed: FMI=%d", fmi);
  }
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
