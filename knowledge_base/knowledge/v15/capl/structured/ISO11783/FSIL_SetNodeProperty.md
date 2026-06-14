# FSIL_SetNodeProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_SetNodeProperty( char propertyName[], long propertyValue); // form 1
long FSIL_SetNodeProperty( dbNode fs, char propertyName[], long propertyValue); // form 2
long FSIL_SetNodeProperty( char propertyName[],char propertyValue[]); // form 3
long FSIL_SetNodeProperty( dbNode fs, char propertyName[], char propertyValue[]); // form 4
```

## Description

Changes an internal property of the File Server node.

## Parameters

| Name | Description |
|---|---|
| fs | File Server simulation node to apply the function. |
| propertyName | Name of the property (see Functional Properties of FS IL and Network Properties of FS IL). |
| propertyValue | New value for the property |

## Example

Example form 2, 4

```c
void SetNodeProperties()
{
  // Set File Server version 3
  FSIL_SetNodeProperty(FS, "fsVersion", 3);
  // Set root directory for file server volumes
  FSIL_SetNodeProperty (FS, "rootDirectory", "ISOBUS_FSRootDir");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3) | ✔ (form 1, 3) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
