# CarMaker_InvokeCommand

> Category: `CarMaker` | Type: `function`

## Syntax

```c
long CarMaker_InvokeCommand(char command[], char result[], long resultSize);
```

## Description

Synchronously calls a generic command and stores the result.

## Parameters

| Name | Description |
|---|---|
| command | CarMaker script command including parameters. |
| result | Output buffer for the result text. |
| resultSize | Size of the output buffer. |

## Return Values

APO return code

## Example

```c
long status;
char result[200];
status = CarMaker_InvokeCommand("TestMgr get Result", result, elcount(result));
write("Status: 0x%lx  Result: \"%s\"", status, result);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 SP2 | — | — | — | 5.0 SP2 |
| Restricted To | — | CarMaker | — | — | — | CarMaker |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
