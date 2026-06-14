# A664isICMP

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664isICMP (a664Frame aFrame, dbNode NodeName) (1)
long A664isICMP (a664Frame aFrame, dword dstIP, word VLid) (2)
```

## Description

This function returns the ICMP type and code for a packet. The intended use case is a check for an expected ICMP packet in an on-handler. The packet is checked according to the following rules:

## Parameters

| Name | Description |
|---|---|
| aFrame | The frame object of type a664Frame to be checked. |
| NodeName | (1) This is the name of a node from the assigned DBC. The DBC must be an AFDX DBC file and the necessary attributes must exist. |
| dstIP | (2) destination IP address to be used for check. |
| VLid | (2) VLId to be used for check. |

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
