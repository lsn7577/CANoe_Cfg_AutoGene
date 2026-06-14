# CarMaker_GetNamedValue

> Category: `CarMaker` | Type: `function`

## Syntax

```c
long CarMaker_GetNamedValue(char name[], char buffer[], long bufferSize);
```

## Description

Copies the current value with the given name into the buffer provided by the caller. If the size of the buffer is insufficient the value will be truncated and zero terminated.

## Parameters

| Name | Description |
|---|---|
| name | Name of the named value. |
| buffer | Output buffer for the current value. |
| bufferSize | Size of the output buffer. |

## Return Values

APO return code

## Example

```c
void printStatus()
{
  char statusBuf[256]= "";
  gErrorState = CarMaker_GetNamedValue("Status", statusBuf, elcount(statusBuf));
  write("Status: \"%s\"", statusBuf);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | CarMaker | — | — | — | CarMaker |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
