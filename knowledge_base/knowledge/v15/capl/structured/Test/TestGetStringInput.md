# TestGetStringInput

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetStringInput (char aAnswer[], dword aAnswerLen);
```

## Description

Returns the result of the last successful call of TestWaitForStringInput.

## Parameters

| Name | Description |
|---|---|
| aAnswer | Variable in which the entry of the user must be accepted. |
| aAnswerLen | Length of variable which has to accept the user entry. |

## Example

```c
// ask for the users name and report it in the Write Window
char answer[100];
if (1== TestWaitForStringInput("Please enter your name", 5000))
{
TestGetStringInput(answer, 100);
   Write("name = %s", answer);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
