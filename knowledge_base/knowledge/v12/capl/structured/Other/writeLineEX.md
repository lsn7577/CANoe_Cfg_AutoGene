# writeLineEX

> Category: `Other` | Type: `function`

## Syntax

```c
void writeLineEx(long sink, dword severity, char format[], ...)
```

## Description

Writes the text into a new line of the specified window, into a page of the CANoe Write Window or into a logging file.

To write into the CANoe Trace Window please activate the CAPL System Message in the predefined filters of the Trace Window.

## Parameters

| Name | Description |
|---|---|
| -3 | Trace Window |
| -2 | Output to the logging file (only in ASC format and if the CAPL node is inserted in the Measurement Setup in front of the Logging Block) |
| -1 | Reserved |
| 0 | Output to the System page of the Write Window |
| 1 | Output to the CAPL page of the Write Window |
| 4 | Output to the Test page of the Write Window |

## Return Values

—

## Availability

| Since Version |
|---|
