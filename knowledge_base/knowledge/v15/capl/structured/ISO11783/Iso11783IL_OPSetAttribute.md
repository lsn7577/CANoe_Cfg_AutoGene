# Iso11783IL_OPSetAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPSetAttribute( dword objectID, dword attributeID, long value ); // form 1
long Iso11783IL_OPSetAttribute( dword objectID, dword attributeID, long value, long options ); // form 2
long Iso11783IL_OPSetAttribute( dbNode implement, dword objectID, dword attributeID, long value, long options ); // form 3
```

## Description

The function sets an attribute value of an object. The object must exist in the object pool and support the attribute ID. If the Object Pool API is active, the Change Attribute command (175) is sent to the Virtual Terminal. This can be suppress with Bit 0 in options.

## Parameters

| Name | Description |
|---|---|
| objectID | object ID of an object in the object pool |
| attributeID | attribute ID, see ISO11783-6 |
| value | new value |
| options | options Bit 0 and 1 = 0: send Change Attribute Value command if parameters are valid Bit 0 and 1 = 1: suppress Change Attribute Value command Bit 0 and 1 = 2: force sending Change Attribute Value command even parameters are invalid Bit 0 and 1 = 3: reserved |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPSetAttribute( 
 1000, 3, 20 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2 9.0: form 3 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3) | ✔ (form 3) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3) | ✔ (form 3) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
