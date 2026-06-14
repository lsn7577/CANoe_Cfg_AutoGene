# TCIL_GetValuePresentationData

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetValuePresentationData(dbNode client, dword ddi, dword elementNumber,dword idOfDVP, long offset, float scale, dword numberOfDecimals, dword designatorBufferSize, char designatorBuffer[]); // form 1: deprecated with 13
long TCIL_GetValuePresentationData(dbNode client, dword ddi, dword elementNumber,dword idOfDVP, long offset, float scale,dword numberOfDecimals, char designatorBuffer[]); // form 2
long TCIL_GetValuePresentationData(dword addressClient, dword ddi, dword elementNumber,dword idOfDVP, long offset, float scale,dword numberOfDecimals, char designatorBuffer[]); // form 3
long TCIL_GetValuePresentationData(dbNode tc, dbNode client, dword ddi, dword elementNumber,dword idOfDVP, long offset, float scale, dword numberOfDecimals,dword designatorBufferSize, char designatorBuffer[]); // form 4: deprecated with 13
long TCIL_GetValuePresentationData(dbNode tc, dbNode client, dword ddi, dword elementNumber,dword idOfDVP, long offset, float scale,dword numberOfDecimals, char designatorBuffer[]); // form 5
long TCIL_GetValuePresentationData(dbNode tc, dword addressClient, dword ddi, dword elementNumber,dword idOfDVP, long offset, float scale,dword numberOfDecimals, char designatorBuffer[]); // form 6
```

## Description

Returns all properties (id, offset, scale, numberDecimals, designator) of the ValuePresentation object referenced by the DeviceProcessData (DPD) or DeviceProperty (DPT) object defined by DDI/elementNumber.

Form 5 and 6 applicable in test module / test unit only.

## Parameters

| Name | Description |
|---|---|
| tc | TC simulation node to apply the function. |
| client | TC client node the data entity belongs to. |
| addressClient | Address of the TC client node the data entity belongs to. |
| ddi | Data dictionary identifier of DPD/DPT object, 0x0000..0xFFFF. |
| elementNumber | Element number of DPD/DPT object, 0x000..0xFFF. |
| idOfDVP | ID of the referenced DVP object. 0xFF means no DVP object is referenced. |
| offset | Property offset of the referenced DVP object. |
| scale | Property scale of the referenced DVP object. |
| numberOfDecimals | Property numberOfDecimals of the referenced DVP object. |
| designatorBufferSize | Size of the return buffer. |
| designatorBuffer | Return buffer. Contains the designator of the DVP ojects as a string. |

## Example

Example form 5

```c
long result;
char designator[256];
dword idOfDVP, numOfDecimals;
long offset;
float scale;
// Retrieve all properties of the DVP object used by the DPD with DDI=17 and elementNumber=3
// from DDOP uploaded by Sprayer to TC
result = TCIL_GetValuePresentationData(TC, Sprayer, 17, 3, idOfDVP, offset, scale, numOfDecimals, 256, designator);
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
