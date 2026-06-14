# TestAddRange

> Category: `Test` | Type: `function`

## Syntax

```c
TestAddRange(long handle, double minValue, double maxValue);
```

## Description

This function adds a new range that is allowed for dialog input. This can be a minimum/ maximum for a numerical value or a minimum/ maximum length of a string or byte array.

## Parameters

| Name | Description |
|---|---|
| Handle | The handle of the dialog. |
| minValue | The minimum of the input. |
| maxValue | The maximum of the input. |

## Return Values

—

## Example

```c
handle = TestCreateValueInputRange("Test Text", "Test Caption", "Test Value Input Range Timeout");
TestAddRange(handle, 0, 5);
TestWaitForInput(handle, 5000);
write("Result: %f", TestGetValueInput());
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | 14 | 3.0 |
| Restricted To | — | Test nodes | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
