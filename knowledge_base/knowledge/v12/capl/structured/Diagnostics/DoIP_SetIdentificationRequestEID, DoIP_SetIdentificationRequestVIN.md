# DoIP_SetIdentificationRequestEID, DoIP_SetIdentificationRequestVIN

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetIdentificationRequestEID(byte EID[]);
```

## Description

Configures the Vehicle Identification Request Message sent by a tester.

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

| Since Version |
|---|
