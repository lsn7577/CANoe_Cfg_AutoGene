# Iso11783OPSetAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSetAttribute( dword ecuHandle, dword objectID, dword attributeID, long value );
long Iso11783OPSetAttribute( dword ecuHandle, dword objectID, dword attributeID, long value, long options );
```

## Description

The function sets an attribute value of an object. The object must exist in the object pool and support the attribute ID. If the Object Pool API is active, the Change Attribute command (175) is sent to the Virtual Terminal. This can be suppress with Bit 0 in options.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU (must be created with Iso11783CreateECU) |
| objectID | Object ID of an object in the object pool |
| attributeID | Attribute ID, see ISO11783-6 |
| value | New value |
| options | OptionsBit 0 = 1: suppress Change Attribute Value command |

## Example

```c
Iso11783OPSetAttribute( 
 handle, 1000, 3, 20 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
