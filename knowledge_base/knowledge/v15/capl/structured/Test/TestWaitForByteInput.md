# TestWaitForByteInput

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForByteInput(char text[], char caption[], char info[]); // form 1
long TestWaitForByteInput(char text[], char caption[], char info[], dword timeout); // form 2
```

## Description

This function opens a dialog for byte array input. Optionally you can set some timeout in ms. Afterwards the dialog will be closed. You can optionally define some default input for the dialog.

## Parameters

| Name | Description |
|---|---|
| Text | Text to be displayed in the entry dialog. |
| Caption | The title of the dialog. |
| Info | Further information to be shown |
| Timeout | Optional timeout for the dialog in ms. |

## Example

```c
return = TestWaitForByteInput("Test Text", "Test Caption", "Test Byte Input", 0);
TestGetByteInput(resultByte, elcount(resultByte));

return = TestWaitForByteInput("Test Text", "Test Caption", "Test Byte Input Timeout", 5000);
TestGetByteInput(resultByte, elcount(resultByte));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | 14 | 3.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
