# TCIL_SetTCStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_SetTCStatus(dword cycleTime); // form 1
long TCIL_SetTCStatus(dword cycleTime, pg PD); // form 2
long TCIL_SetTCStatus(dbNode tc, dword cycleTime); // form 3
long TCIL_SetTCStatus(dbNode tc, dword cycleTime, pg pgPD); // form 4
```

## Description

This function changes the content and cycle time of the TC Status message.

Form 1 and 3: The content of TC Status message stays unchanged; only the cycle time is changed.

## Parameters

| Name | Description |
|---|---|
| tc | TC simulation node to apply the function |
| cycleTime | Cycle time of the TC Status message [ms] (default: 1000) |
| pgPD | Content of this message is used by the following TC Status messages sent by the TC IL |

## Example

Example form 3

```c
pg PD pgPD;
pgPD.TCFunctionTCtoECU = 254;
pgPD.SourceAdressOfActiveWSM = 1;
pgPD.VisibleDataAlarmMaskID = 1000;
pgPD.VisibleSoftKeyMaskID = 2000;
pgPD.TCBusyCode1 = 0;
pgPD.TCBusyCode2 = 0;
pgPD.TCBusyCode3 = 0;
pgPD.TCBusyCode4 = 0;
pgPD.TCBusyCode8 = 0;
pgPD.TCFunctionCode = 0;
if (TCIL_SetTCStatus( TC, 1000, pgPD ) < 0)
{
  TestStepFail("Failed to set TC Status");
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
