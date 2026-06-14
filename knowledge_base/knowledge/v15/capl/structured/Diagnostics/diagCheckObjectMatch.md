# diagCheckObjectMatch

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagCheckObjectMatch( diagRequest request, diagResponse response);
```

## Description

Checks if the response service id is a valid (positive or negative) response for the request.

## Parameters

| Name | Description |
|---|---|
| request | Diagnostics request |
| response | Diagnostics response |

## Return Values

Error code

## Example

```c
DiagRequest AirbaContr_Read req;
DiagResponse AirbaContr_Read resp;

if( 1 == diagCheckObjectMatch( req, resp))
write( "Request and response match!");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 7.1 | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
