# A664InitPayload

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664InitPayload (a664Message aMessage)
```

## Description

The payload section (excluding sequence number) of an AFDX message is set using the current Tx-values of the internal signal list (CANdb++). These are typically set by CAPL signal value assignments, panels, signal generators, start value etc.

The message must be defined in the database and must contain signals (no protocol oriented types).

## Parameters

| Name | Description |
|---|---|
| aMessage | The message object to be initialized. |

## Example

```c
a664Message TESTMSG_ALLTYPES testMsg = { msgChannel = 1};
a664InitPayload (testMsg); 	// set payload to last known signal values
a664TriggerMessage(testMsg, 1);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP4 | 9.0 SP4 | — | — | — | — |
| Restricted To | AFDX | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
