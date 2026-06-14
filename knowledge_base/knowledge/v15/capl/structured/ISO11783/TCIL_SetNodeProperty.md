# TCIL_SetNodeProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_SetNodeProperty( char propertyName[], long propertyValue); // form 1
long TCIL_SetNodeProperty( dbNode tc, char propertyName[], long propertyValue); // form 2
```

## Description

Changes an internal property of the node.

## Parameters

| Name | Description |
|---|---|
| tc | TC simulation node to apply the function |
| propertyName | Name of the property (see Functional Properties of TC IL and Network Properties of TC IL). |
| propertyValue | New value for the property |

## Example

Example form 2

```c
void SetLanguageToEnglish()
{
  TCIL_SetNodeProperty(TC, "languageCode", 0x656E); // 'en'
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
