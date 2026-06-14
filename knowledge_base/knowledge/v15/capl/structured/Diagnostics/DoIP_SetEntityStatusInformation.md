# DoIP_SetEntityStatusInformation

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetEntityStatusInformation(long nodeType, dword maxRequestSize);
```

## Description

Configures the response sent for an entity status request.

## Parameters

| Name | Description |
|---|---|
| nodeType | -1: do not send a response for the request (default) 0: gateway 1: node others: reserved |
| maxRequestSize | 0: do not send this optional parameter in a response 0xFFFFFFFF: send a value that is supported by this implementation. Currently 16777216 is sent (i.e. 16 MiB) other: value sent in the response |

## Return Values

—

## Example

```c
// The ECU simulation will return type "node" and a maximum length supported
// by this protocol implementation
DoIP_SetEntityStatusInformation( 1, 0xFFFFFFFF);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | — | — | — | 2.1 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
