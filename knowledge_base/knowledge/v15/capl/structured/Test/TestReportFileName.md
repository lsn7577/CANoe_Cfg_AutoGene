# TestReportFileName

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportFileName (char data name[]);
```

## Description

Sets the name and path of a report file.In the CANoe GUI the name and path of a report file can be set. With this function these settings can be overwritten.

## Parameters

| Name | Description |
|---|---|
| data name | Name and path of the report file. Without path specification, the directory of the CANoe configuration file is used. The extension .xml, .html or .vtestreport is added automatically. |

## Return Values

—

## Example

```c
void MainTest()
{
   // report is written in a file with the name ‚DynamicName’ beside the configuration
   TestReportFileName("DynamicName");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
