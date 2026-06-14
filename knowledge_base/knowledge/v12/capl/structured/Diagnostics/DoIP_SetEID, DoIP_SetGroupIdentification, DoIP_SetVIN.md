# DoIP_SetEID, DoIP_SetGroupIdentification, DoIP_SetVIN

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetEID(byte EID[]);
```

## Description

Configures the Vehicle Announcement/Vehicle Identification Response Message sent by a vehicle simulation.

If these functions are used in combination with DiagInitEcuSimulation, the functions must be called in on prestart. Otherwise the functions have no effect.

Reason: The DoIP.DLL is initialized in a ECU simulation after on prestart but before on start.

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

| Since Version |
|---|
