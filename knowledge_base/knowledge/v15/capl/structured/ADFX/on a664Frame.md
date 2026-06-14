# on a664Frame

> Category: `ADFX` | Type: `event`

## Description

The event procedure on a664Frame is called on every AFDX packet if the following conditions are fulfilled:

or

Additional information related to this event is available via the selectors. The keyword this is available within an on a664Frame procedure to access the data of the AFDX event that has just been received.

## Example

Calling conventions for the on a664Frame handler.

Convention

Comment

on a664Frame 0xA1

Event with VLId 0xA1 (hexadecimal).

on a664Frame 123

Event with VLId 123 (decimal).

on a664Frame *

Event with any VLId.

on a664Frame MsgChannel1.*

Event with any VLId on channel 1.

on a664Frame MsgChannel1.0xA1

Event with VLId 0xA1 (hexadecimal) on channel 1.

on a664Frame MsgChannel1.123

Event with VLId 123 (decimal) on channel 1.

on a664Frame ICMP

on a664Frame MsgChannel1.ICMP

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 | 9.0 | — | — | — | —✔ |
| Restricted To | AFDX | AFDX | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |

## Selectors

| Selectors for AFDX-Frames | ../CAPLfunctionsAFDXSelectors.htm |
|---|---|
