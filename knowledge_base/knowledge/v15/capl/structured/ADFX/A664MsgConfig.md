# A664MsgConfig

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664MsgConfig (a664Frame aFrame, dword IpFrag, dword Line, dword SubVlId) (1)
long A664MsgConfig (a664Message aMessage, dword IpFrag, dword Line, dword SubVlId) (2)
```

## Description

Configure the Tx parameters for a given a664Frame or a664Message.

## Parameters

| Name | Description |
|---|---|
| IpFrag | (this parameter is ignored for a664Frame): 0 no IP fragmentation 1 message may be fragmented |
| Value | Short Name Description Interface_ID updated? Message duplicated? |
| 0 | — Line assignment is derived from the VL settings (selector LineSelect) • • |
| 1 | ForceA Use line A • — |
| 2 | ForceB Use line B • — |
| 3 | ForceAB Use both lines • • |
| SubVlId | Specify the SubVLid, used for this message or frame. The allowed value range is 1 .. 4. The value is not checked against the selector SubVLNr. |

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
