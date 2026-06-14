# TestWaitForTextEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForTextEvent(char aText[], dword aTimeout);
```

## Description

Waits for the signaling of the specified textual event from the individual test module. A signaling from another test module does not effect this wait instruction.

Should this event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| aText | Any (meaningful) textual event name |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout controlling) |

## Example

```c
// waits for the occurrence of text event „ErrorFrame occurred!“
long result;
result = TestWaitForTextEvent("ErrorFrame occurred!", 3000);

// handler ‘on errorFrame’ signals event
on errorFrame
{
   TestSupplyTextEvent("ErrorFrame occurred!");
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
