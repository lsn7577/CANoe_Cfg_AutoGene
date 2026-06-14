# VTIL_EditStringValue, VTIL_ChangeStringValueMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_EditStringValue(dword objectId, char value[], dword duration); // form 1
long VTIL_EditStringValue(dword objectId, char value[], dword duration, dword option); // form 2
long VTIL_EditStringValue(dbNode vt, dword objectId, char value[], dword duration); // form 3
long VTIL_EditStringValue(dbNode vt, dword objectId, char value[], dword duration, dword option); // form 4
long VTIL_ChangeStringValueMsg(dword objectId, char value[]); // form 5
long VTIL_ChangeStringValueMsg(dbNode vt, dword objectId, char value[]); // form 6
```

## Description

Editing of an Input String object.

The VTIL_EditStringValue methods simulate the selection, opening, value modification and closing of the Input String object. The corresponding VT messages are sent. If the object is already selected or opened for input, then the steps Select, Open and Close are skipped.

The VTIL_ChangeStringValueMsg methods send only the VT Change String Value message (without influencing any button or input object and without triggering any event in the Virtual Terminal).

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| objectId | Input object ID |
| value | New string value |
| duration [ms] | After this duration the edit process ends |
| option | 0: No additional option 1: Edit object even it is not part of the active Data/Alarm Mask |

## Example

Example form 3 and 6

```c
long result;
result = VTIL_EditStringValue (VT, 301, "text", 2000);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2102: TestStepFail("Invalid object!"); break;
  case -2104: TestStepFail("Currently there is no active Working Set!"); break;
  case -2106: TestStepFail("Currently there is no active Data or Alarm mask!"); break;
  case -2115: TestStepFail("VT works in passiv mode therefore you cannot select objects!"); break;
  case -2117: TestStepFail("Failed to open object for editing!"); break;
  case -2118: TestStepFail("Object is no Input String object!"); break;
  case -2120: TestStepFail("Failed to edit object because it is disabled!"); break;
  case -2121: TestStepFail("Button is not available in the current  context!"); break;
  default: TestStepFail("Unexpected error!"); break;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1, 3, 5, 6 10.0 SP4: form 2, 4 | 13.0 | — | — | 2.1: form 3, 6 2.2 SP3: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4, 6 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2, 5) | ✔ (form 1, 2, 5) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4, 6) | ✔ (form 3, 4, 6) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4, 6) | ✔ (form 3, 4, 6) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
