# A664ResizeMessage

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664ResizeMessage (a664Message aMessage, word newSize)
```

## Description

The message object’s payload area is resized to match the new payload size.

This affects the selectors Length and AfdxLength. If the current aMessage headers are valid (see AFDX packet validation rules), the corresponding header content is adapted as well (IP and UDP headers).

## Parameters

| Name | Description |
|---|---|
| aMessage | Message object to be resized. |
| newSize | New payload size (without counting sequence number) in range 0..8192. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 | 9.0 | — | — | — | — |
| Restricted To | AFDX | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
