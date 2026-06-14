# A664SetChecksum

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664SetChecksum (a664Frame aFrame, dword Rule)
```

## Description

This function calculates and sets the checksum in the specified aFrame according to the defined checksum rule.

## Parameters

| Name | Description |
|---|---|
| aFrame | The a664Frame object where the checksum is calculated and stored. |
| Rule | Defines the checksum rule based on the protocol type. 1 – IP checksum 2 – ICMP checksum 3 – UDP checksum |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | — | — | — | — |
| Restricted To | AFDX | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
