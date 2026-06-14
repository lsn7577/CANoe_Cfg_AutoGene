# TCIL_ResetTCStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ResetTCStatus( ); // form 1
long TCIL_ResetTCStatus(dbNode tc); // form 2
```

## Description

This function reverts changes made by TCIL_SetTCStatus and turns back to the default behavior of the Task Controller IL.

## Parameters

| Name | Description |
|---|---|
| tc | TC simulation node to apply the function |

## Return Values

—

## Example

Example form 2

```c
pg TC12 tc12;
tc12.TCFunctionTCtoECU = 254;
tc12.SourceAdressOfActiveWSM = 1;
tc12.VisibleDataAlarmMaskID = 1000;
tc12.VisibleSoftKeyMaskID = 2000;
tc12.TCBusyCode1 = 0;
tc12.TCBusyCode2 = 0;
tc12.TCBusyCode3 = 0;
tc12.TCBusyCode4 = 0;
tc12.TCBusyCode8 = 0;
tc12.TCFunctionCode = 0;
if (TCIL_SetTCStatus( TC, 1000, tc12 ) < 0)
{
  TestStepFail("Failed to set TC Status");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
