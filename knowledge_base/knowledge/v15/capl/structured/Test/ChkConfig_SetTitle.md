# ChkConfig_SetTitle

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkConfig_SetTitle (dword aCheckId, char aTitle[]);
```

## Description

Sets the title of a check.

The check is displayed in the Write Window and the test report with this title.

## Parameters

| Name | Description |
|---|---|
| aCheckId | Identifier of the check |
| aTitle | Title of the check |

## Example

```c
// set title of the check
dword mCheckId;
mCheckId = ChkCreate_Timeout(1000);
ChkConfig_SetTitle(mCheckId, "Check Timeout");
ChkControl_Start(mCheckId);
TestCheck tc;
tc = TestCheck::CreateTimeout(1000);
tc.SetTitle("Check Timeout");
tc.Start();
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
