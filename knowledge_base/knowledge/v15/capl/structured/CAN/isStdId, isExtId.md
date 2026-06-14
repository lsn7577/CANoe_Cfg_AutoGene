# isStdId, isExtId

> Category: `CAN` | Type: `function`

## Syntax

```c
long isStdId(dword id);
long isStdId(message m);
long isExtId(dword id);
long isExtId(message m);
```

## Description

Checks parameter for extended identifier (29 bit) or standard identifier (11 Bit).

## Parameters

| Name | Description |
|---|---|
| message | Variable of type message |
| id | Id part of a message |

## Return Values

1 if check was successful, else 0

## Example

```c
...
if(isExtId(this))
write("extended identifier");
else
write("standard identifier");
or
std = isStdId(m100.id);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
