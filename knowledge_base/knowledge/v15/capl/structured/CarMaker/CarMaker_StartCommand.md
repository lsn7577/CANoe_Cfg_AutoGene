# CarMaker_StartCommand

> Category: `CarMaker` | Type: `function`

## Syntax

```c
long CarMaker_StartCommand(char host[char command[]);
```

## Description

Asynchronously calls a generic command and ignores the result.

## Parameters

| Name | Description |
|---|---|
| command | CarMaker script command including parameters. |

## Return Values

APO return code

## Example

```c
// stop test series after the current TestRun has ﬁnished
gErrorState = CarMaker_StartCommand("TestMgr stop");
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
