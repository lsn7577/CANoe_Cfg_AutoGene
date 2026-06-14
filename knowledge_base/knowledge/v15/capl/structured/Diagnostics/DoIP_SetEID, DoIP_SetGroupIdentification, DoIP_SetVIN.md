# DoIP_SetEID, DoIP_SetGroupIdentification, DoIP_SetVIN

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetEID(byte EID[]);
void DoIP_SetGroupIdentification(byte GID[], dword furtherActionRequired, dword VINGIDsyncStatus);
void DoIP_SetVIN(byte VIN[]);
void DoIP_SetVIN(char VIN[]);
```

## Description

Configures the Vehicle Announcement/Vehicle Identification Response Message sent by a vehicle simulation.

## Parameters

| Name | Description |
|---|---|
| EID | Send this entity ID in the message, e.g. a MAC address. |
| GID | Send this group identity in the message, e.g. a MAC address. |
| furtherActionRequired | 0: No further action is required (default) |
| VINGIDsyncStatus | 0: VIN and GID are synchronized (default)0x10: VIN and GID are NOT synchronized; the tester should repeat the Vehicle Identification Request. |
| VIN | Vehicle Identification Number sent in the message. |

## Return Values

—

## Example

These values can also be configured in the DoIP.INI file.

```c
// Set the entity and group IDs
BYTE eid[6] = { 0x20, 0x11, 0x22, 0x33, 0x44, 0x55};
BYTE gid[6] = { 0x20, 0x11, 0x22, 0x33, 0xFF, 0xFF};
DoIP_SetEID( eid);
// Indicate that VIN and GID are not synchronized yet, i.e. the tester shall repeat
// the Vehicle Identification Request after some time
DoIP_SetGroupIdentification( gid, 0, 0x10);
if( gSetVINasBytes)
{
  // Alternatively, set the VIN using a raw byte stream
  BYTE rawVIN[17] = { 0xFF, 0xFF, 0xFF, 0xFF,    0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,    0xFF, 0xFF, 0xFF, 0xFF, 0xFF };
  DoIP_SetVIN( rawVIN);
} else
{
  // Set the VIN using its textual representation
  DoIP_SetVIN("VECT0RVEH1CLE1234");
}
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
