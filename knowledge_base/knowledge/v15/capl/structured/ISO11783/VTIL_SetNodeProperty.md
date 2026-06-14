# VTIL_SetNodeProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SetNodeProperty( char propertyName[], long propertyValue); // form 1
long VTIL_SetNodeProperty( dbNode vt, char propertyName[], long propertyValue); // form 2
long VTIL_SetNodeProperty( char propertyName[],char propertyValue[]); // form 3
long VTIL_SetNodeProperty( dbNode vt, char propertyName[], char propertyValue[]); // form 4
```

## Description

Changes an internal property of the node.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function |
| propertyName | Name of the property (see Properties of VT IL and Network Properties of VT IL) |
| propertyValue | New value for the property |

## Example

Example form 2, 4

```c
void SetNodeProperties()
{
  //Set language to English
  VTIL_SetNodeProperty(VT, "languageCode", 0x656E);
  // Object Pools have to be stored in the subdirectory "OP_VT1"
  VTIL_SetNodeProperty(VT, "locationOfStoredObjectPools", "OP_VT1");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1, 2 9.0 SP4: form 3, 4 | 13.0 | — | — | 2.1: form 2 2.1 SP4: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3) | ✔ (form 1, 3) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
