# VTIL_SetVTStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SetVTStatus(dword cycleTime); // form 1
long VTIL_SetVTStatus(dword cycleTime, pg VT12 pgWithNewContent); // form 2
long VTIL_SetVTStatus(dbNode vt, dword cycleTime); // form 3
long VTIL_SetVTStatus(dbNode vt, dword cycleTime, pg VT12 pgWithNewContent); // form 4
```

## Description

Forms (1) and (3): This function changes the cycle time of the VT Status message.The content of VT Status message stays unchanged.

Forms (2) and (4): This function changes the content and cycle time of the VT Status message.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| cycleTime | Cycle time of the VT Status message [ms] (default: 1000) |
| pgWithNewContent | Content of this message is used by the following VT Status messages sent by the VT IL |

## Example

Example form 3, 4

```c
pg VT12 vt12;
vt12.VTFunctionVTtoECU = 254;
vt12.SourceAdressOfActiveWSM = 1;
vt12.VisibleDataAlarmMaskID = 1000;
vt12.VisibleSoftKeyMaskID = 2000;
vt12.VTBusyCode1 = 0;
vt12.VTBusyCode2 = 0;
vt12.VTBusyCode3 = 0;
vt12.VTBusyCode4 = 0;
vt12.VTBusyCode8 = 0;
vt12.VTFunctionCode = 0;
if (VTIL_SetVTStatus( VT, 1000, vt12 ) < 0)
{
  TestStepFail("Failed to set VT Status");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
