# coTfsLoadDeviceDescription

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLoadDeviceDescription( dword nodeId, char fileName[] );
```

## Description

This function reads an EDS, DCF or XML file. This allows the interpretation of index and sub index during SDO accesses, so that object names can be displayed in plain text.

The object names can be deleted with coTfsClearObjectName.

## Parameters

| Name | Description |
|---|---|
| nodeId | Node-ID of the relevant node or 0 if all nodes are used. If node specific entries should be added, these have a higher priority on display. |
| fileName[] | Name of the file to be read, relative to your CANoe configuration. |

## Return Values

Error code

## Example

```c
/* load for CANopen device with node ID 112 the eds file "coslave.eds" (path is relative to configuration folder) */
if (coTfsLoadDeviceDescription(112, "coslave.eds") != 1)
{
  /* file could not be loaded, either it does not exist or it is faulty */
} /* if */
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
