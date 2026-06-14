# TestWaitForInput

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForInput(long handle); // form 1
long TestWaitForInput(long handle, dword timeout); // form 2
long TestWaitForInput(long handle, dword timeout, dword defaultIndex); // form 3
```

## Description

After you have created a value table or range dialog use this function to open the dialog.

## Parameters

| Name | Description |
|---|---|
| Handle | The handle of the dialog. |
| DefaultIndex | The index of the value is marked on dialog opening. |
| Timeout | Optional timeout for the dialog in ms. |

## Example

```c
handle = TestCreateValueInputTable("Test Text", "Test Caption", "Test Value Input Table Timeout");
TestAddValueTableEntry(handle, 9);
return = TestWaitForInput(handle, 5000);
write("Result: %f", TestGetValueInput());
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
