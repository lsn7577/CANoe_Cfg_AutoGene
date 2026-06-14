# TestCreateStringInputTable, TestCreateValueInputTable

> Category: `Test` | Type: `function`

## Syntax

```c
TestCreateStringInputTable(char text[], char caption[], char info[]);
TestCreateValueInputTable(char text[], cahr caption[], char info[]);
```

## Description

This function creates a selection dialog. To add a value table entry, use the command TestAddValueTableEntry or TestAddStringTableEntry. After all entries are added the dialog can be opened by the command TestWaitForInput.

## Parameters

| Name | Description |
|---|---|
| Text | Text to be displayed in the entry dialog |
| Caption | The title of the dialog. |
| Info | Further information to be shown. |

## Return Values

The handle of the dialog.

## Example

```c
handle = TestCreateStringInputTable("Test Text", "Test Caption", "Test String Input Table Timeout");
TestAddStringTableEntry(handle, "Test Entry");
TestWaitForInput(handle, 5000);
TestGetStringInput(resultStr, elcount(resultStr));

handle = TestCreateValueInputTable("Test Text", "Test Caption", "Test Value Input Table Timeout");
TestAddValueTableEntry(handle, 9);
TestWaitForInput(handle, 5000);
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
