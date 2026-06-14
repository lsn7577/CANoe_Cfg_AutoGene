# TestCreateInputRange

> Category: `Test` | Type: `function`

## Syntax

```c
TestCreateStringInputRange(char text[], char caption[], char info[]);
TestCreateValueInputRange(char text[], char caption[], char info[]);
TestCreateByteInputRange(char text[], char caption[], char info[]);
```

## Description

This function creates an input dialog. For adding a new range to define the input use the command TestAddRange. After all ranges are added the dialog can be opened by the command TestWaitForInput.

## Parameters

| Name | Description |
|---|---|
| Text | Text to be displayed in the entry dialog. |
| Caption | The title of the dialog. |
| Info | Further information to be shown. |

## Return Values

The handle of the dialog.

## Example

```c
handle = TestCreateStringInputRange("Test Text", "Test Caption", "Test String Input Range Timeout");
TestAddRange(handle, 0, 5);
TestWaitForInput(handle, 5000);
TestGetStringInput(resultStr, elcount(resultStr));

handle = TestCreateValueInputRange("Test Text", "Test Caption", "Test Value Input Range Timeout");
TestAddRange(handle, 0, 5);
TestWaitForInput(handle, 5000);

handle = TestCreateByteInputRange("Test Text", "Test Caption", "Test Byte Input Range Timeout");
TestAddRange(handle, 0, 5);
TestWaitForInput(handle, 5000);
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
