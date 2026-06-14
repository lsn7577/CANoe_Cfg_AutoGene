# TCIL_GetDesignator

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetDesignator(dbNode client, dword ddi, dword elementNumber, dword unitDesignatorBufferSize, char unitDesignatorBuffer[]); // form 1: deprecated with 13
long TCIL_GetDesignator(dbNode client, dword ddi, dword elementNumber, char unitDesignatorBuffer[]); // form 2
long TCIL_GetDesignator(dword addresClient, dword ddi, dword elementNumber, char unitDesignatorBuffer[]); // form 3
long TCIL_GetDesignator(dbNode tc, dbNode client, dword ddi, dword elementNumber, dword unitDesignatorBufferSize, char unitDesignatorBuffer[]); // form 4: deprecated with 13
long TCIL_GetDesignator(dbNode tc, dbNode client, dword ddi, dword elementNumber, char unitDesignatorBuffer[]); // form 5
long TCIL_GetDesignator(dbNode tc, dword addresClient, dword ddi, dword elementNumber, char unitDesignatorBuffer[]); // form 6
```

## Description

Returns the designator of DeviceProcessData (DPD) or DeviceProperty (DPT) object defined by DDI/elementNumber.

Form 5 and 6 applicable in test module / test unit only.

## Parameters

| Name | Description |
|---|---|
| tc | TC simulation node to apply the function. |
| client | TC client node the data entity belongs to. |
| addressClient | TC client node the data entity belongs to. |
| ddi | Data dictionary identifier, 0x0000..0xFFFF. |
| elementNumber | Element number, 0x000..0xFFF. |
| unitDesignatorBufferSize | Size of the return buffer. |
| unitDesignatorBuffer | Return buffer. Contains the designator as a string. |

## Example

Example form 5

```c
long result;
char designator[256];
// Retrieve the designator for the DPD with DDI=17 and elementNumber=3 from DDOP uploaded by Sprayer to TC
result = TCIL_GetDesignator(TC, Sprayer, 17 /*DDI/, 3 /elementNumber/, designator /buffer/);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 5.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 5, 6 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 2, 3) | ✔ (form 2, 3) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 5, 6) | ✔ (form 5, 6) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 5, 6) | ✔ (form 5, 6) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
