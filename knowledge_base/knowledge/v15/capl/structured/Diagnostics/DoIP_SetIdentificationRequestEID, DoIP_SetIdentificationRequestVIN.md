# DoIP_SetIdentificationRequestEID, DoIP_SetIdentificationRequestVIN

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetIdentificationRequestEID(byte EID[]);
void DoIP_SetIdentificationRequestVIN(char VIN[]);
```

## Description

Configures the Vehicle Identification Request Message sent by a tester.

## Parameters

| Name | Description |
|---|---|
| EID | Send an entity ID in the message, e.g. a MAC address. |
| VIN | Send a Vehicle Identification Number in the message. If this is an empty string, the message will be sent without indicating a specific vehicle. |

## Return Values

—

## Example

The message can also be configured from the DoIP.INI file.

```c
// Send the MAC address 20:11:22:33:44:55 in the VIR message
BYTE eid[6] = { 0x20, 0x11, 0x22, 0x33, 0x44, 0x55};
DoIP_SetIdentificationRequestEID( eid);

// Send a VIN in the VIR message
DoIP_SetIdentificationRequestVIN( "VECT0RVEH1CLE1234");

// Do not address a specific vehicle, i.e. all vehicles shall respond
DoIP_SetIdentificationRequestVIN( "");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP2 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
