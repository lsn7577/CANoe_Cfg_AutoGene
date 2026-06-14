# TestSupplyTextEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestSupplyTextEvent(char aText[]);
```

## Description

Signals the specified event.

Consequently resolves a possibly-active wait condition on this event.

If such a wait condition is active, the corresponding code will be executed immediately. The current function is therefore interrupted and the code will be executed at a later point in time after the TestSupplyTextEvent function call.

## Parameters

| Name | Description |
|---|---|
| aText | Name of the event to be signaled |

## Example

```c
// Signals the occurrence of an Error Frame as a text event
on errorFrame
{
TestSupplyTextEvent("ErrorFrame occurred!")
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
