# TestInfoCell

> Category: `Test` | Type: `function`

## Syntax

```c
void TestInfoCell (long handle, char[] text);
void TestInfoCell (long handle, char[] text, int span);
```

## Description

Adds a cell to a previously created row or header row.

Using this function, a row can be divided in several columns. For each column a separate cell must be added using this function.

The second version creates a cell that spans over several columns.

## Parameters

| Name | Description |
|---|---|
| handle | Handle to the table created by the function TestInfoTable. |
| text | Text to be displayed in the cell. |
| span | Number of columns that a cell should span. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP2 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
