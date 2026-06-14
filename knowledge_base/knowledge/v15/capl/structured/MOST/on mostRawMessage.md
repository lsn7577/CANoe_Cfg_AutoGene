# on mostRawMessage

> Category: `MOST` | Type: `event`

## Description

on mostRawMessage is called on the receipt of MOST frames whose type isn't Normal.

These are RemoteRead, RemoteWrite, Alloc, Dealloc and GetSource. See Selectors for the applicable selectors. The command output(this) can be used for forwarding the message in a node chain.

If the event procedure should only react to messages on channel 1 this is defined as follows:

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 4.0 | 4.0 | — | — | — | —✔ |
| Restricted To | MOST25 | MOST25 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
