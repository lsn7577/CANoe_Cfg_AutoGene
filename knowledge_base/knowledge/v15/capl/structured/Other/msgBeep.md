# msgBeep

> Category: `Other` | Type: `function`

## Syntax

```c
void msgBeep (long soundType);
```

## Description

The msgBeep function plays back a sound predefined by the Windows system. It replaces the previous beep function.

## Parameters

| Name | Description |
|---|---|
| 0 | MB_ICONASTERISK SystemAsterisk |
| 1 | MB_ICONEXCLAMATION SystemExclamation |
| 2 | MB_ICONHAND SystemHand |
| 3 | MB_ICONQUESTION SystemQuestion |
| 4 | MB_OK SystemDefault |
| 5 | Standard beep using the computer speaker (default) |

## Return Values

—

## Example

```c
void sound() {
// Standard signal question
msgBeep (3);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.0 | 3.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
