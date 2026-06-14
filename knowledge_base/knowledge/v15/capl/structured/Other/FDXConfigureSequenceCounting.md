# FDXConfigureSequenceCounting

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXConfigureSequenceCounting(long fdxClientHandle, long mode);
```

## Description

This function sets the behavior with which CANoe should fill out the field seqNrOrDgramLen in the FDX datagram header.

Prerequisite for the function is to configure UPD/IPv4 or UDP/IPv6 as transport layer for the FDX feature.

## Parameters

| Name | Description |
|---|---|
| fdxClientHandle | FDX client for which the sequence counting should be configured. |
| mode | Mode that should set for the Sequence Counting. 0: Automatic mode (default for new connections)The Sequence Counting automatically adapts to the FDX client. 1: EnabledThe Sequence Counting is activated for the client. 2: DisabledThe Sequence Counting is deactivated for this client. |

## Example

Coupling of two CANoe Instances using the FDX Protocol

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3 | 13.0 | — | 14 | 2.2 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
