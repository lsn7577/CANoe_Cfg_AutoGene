# J1939MakeDTC

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939MakeDTC(dword spn, byte fmi, byte oc, dword &dtcValue)
```

## Description

Function generates a DTC from the defined SPN, FMI and OC.

## Parameters

| Name | Description |
|---|---|
| spn | Suspect Parameter Number of the specified DTC. Valid value range: 0x0 – 0x7FFFF. |
| fmi | Failure Mode Identifier of the specified DTC. Valid value range: 0x0 – 0x1F. |
| oc | Occurrence Counter of the specified DTC . Valid value range: 0x0 – 0x7F. |
| dtcValue | The value of the generated DTC block. |

## Example

```c
//Fill DM1 with two DTCs and send it

  pg DM1 myDM1 = {DLC=10, SA=1};
  dword dtc;

  //Activate Protect Lamp (permanent lighting)
  myDM1.word(0) = 0xFF01;

  //Make first DTC (SPN=67890, FMI=16, OC=101)
  J1939MakeDTC(67890, 16, 101, dtc);
  myDM1.dword(2) = dtc;

  //Make second DTC (SPN=123, FMI=11, OC=5)
  J1939MakeDTC(123, 11, 5, dtc);
  myDM1.dword(6) = dtc;

  //Send DM1 message
  output(myDM1);
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
