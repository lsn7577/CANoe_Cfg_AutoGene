# TestWaitForMessage

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMessage(dbMsg aMessage, dword aTimeout);
long TestWaitForMessage(dword aMessageId, dword aTimeout);
long TestWaitForMessage(dword aTimeout);
```

## Description

Waits for the occurrence of the specified message aMessage. Should the message not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no message is specified the wait condition is resolved on any message.

## Parameters

| Name | Description |
|---|---|
| aMessage | Message that should be awaited |
| aMessageId | Numeric ID of the message that should be awaited |
| aTimeout | Maximum time that should be waited [ms] (Transmission of 0: no timeout controlling) |

## Example

```c
// waits for the occurrence of message ‚VehicleMotion’
long result;
result = TestWaitForMessage(VehicleMotion, 2000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
