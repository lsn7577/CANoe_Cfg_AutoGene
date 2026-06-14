# MediaCreateMultiplexer

> Category: `Media` | Type: `function`

## Syntax

```c
dword MediaCreateMultiplexer(char outputSubtype[])
```

## Description

Creates a multiplexor for the provided output media subtype. For a list of subtypes, see Major Media Types / Subtypes.

## Parameters

| Name | Description |
|---|---|
| outputSubtype | The media subtype describing the format of the output (multiplex) stream. Currently supported subtype: StreamFormat_MPEG2Transport. The Major Type for multiplex streams is always MajorType_Stream. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | — |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | — |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | — |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | — |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | — |
| 32-Bit | — | ✔ | ✔ | N/A | — | — |
| 64-Bit | — | ✔ | ✔ | — | — | — |
