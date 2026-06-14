# on a664Message

> Category: `ADFX` | Type: `event`

## Description

The event procedure on a664Message is called on every AFDX message if the following conditions are fulfilled:

Additional information related to this event is available via the selectors. The keyword this is available within an on a664Message procedure, to access the data of the AFDX event that has just been received.

## Example

Calling conventions for the on a664Message handler

Convention

Comment

event with Id 0x30e40021 (hexadecimal)

event with Id 123423 (decimal)

event with Id from assigned database

event with any Id

event with any Id on channel 1

event with Id 0x30e40021 (hexadecimal) on channel 1

event with Id 123423 (decimal) on channel 1

event with Id from assigned database on channel 1

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

| Selectors for AFDX messages | ../CAPLfunctionsAFDXSelectors.htm |
|---|---|
