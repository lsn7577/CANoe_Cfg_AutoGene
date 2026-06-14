# J1587AppendParameter

> Category: `J1587` | Type: `function`

## Syntax

```c
byte J1587AppendParameter(J1587Message msg /*in/out*/, J1587Param param /*in*/)
```

## Description

Appends a J1587 parameter to a J1708 message.

## Parameters

| Name | Description |
|---|---|
| msg | J1708 message |
| param | returned parameter at the given index |

## Example

```c
J1587Message 50 txMsg;
J1587Param EngineSpeed txEngSpeed;
J1587Param EngineCoolantTemp txEngCool;

J1587AppendParameter(txMsg, txEngSpeed);
J1587AppendParameter(txMsg, txEngCool);

output(txMsg);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 | 7.0 | 13.0 | — | — | — |
| Restricted To | J1587 | J1587 | J1587 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
