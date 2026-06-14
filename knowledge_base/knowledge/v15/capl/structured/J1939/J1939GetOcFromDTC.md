# J1939GetOcFromDTC

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetOcFromDTC(dword dtc)
```

## Description

Function extracts OC from DTC.

## Parameters

| Name | Description |
|---|---|
| dtc | DTC from which an OC is to be extracted. |

## Return Values

Extracted OC.

## Example

```c
on pg DM1
{
  int totalNumOfDTCs, curNumOfDTC;
  dword dtc;
  word fmi, oc;
  dword spn;

  //Iterate over all DTC blocks
  //and extract corresponding SPN, FMI and OC
  totalNumOfDTCs = (this.dlc - 2) / 4;
  for(curNumOfDTC = 0; curNumOfDTC < totalNumOfDTCs; curNumOfDTC++)
  {
    dtc = this.dword(2 + (curNumOfDTC * 4));
    spn = J1939GetSpnFromDTC(dtc);
    fmi = J1939GetFmiFromDTC(dtc);
    oc = J1939GetOcFromDTC(dtc);
    WriteEx(-3, 3, "DM1, DTC Nr. %d: SPN=%d, FMI=%d, OC=%d",
                              curNumOfDTC+1, spn, fmi, oc);
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
