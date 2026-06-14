# DoIP_SetProtocol

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetProtocol (dword protocolID);
```

## Description

Sets protocol version used in DoIP PDUs.

## Parameters

| Name | Description |
|---|---|
| protocolID | 1: Draft version (2010)2: First released ISO standard 2012 (ISO 13400-2 first edition 2012-06-01) 1000: HSFZ protocol Others reserved |

## Return Values

—

## Example

This value can also be configured globally on the diagnostics configuration dialog, DoIP Main Settings.

```c
// Use early draft version of the protocol
DoIP_SetProtocol(1);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP2 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
