# Iso11783IL_SetMessageProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_SetMessageProperty( dbMsg msg, char propertyName[], long propertyValue);
```

## Description

This function sets the internal property of a message.

## Parameters

| Name | Description |
|---|---|
| msg | Message name as defined in the database |
| Value | Description |
| "MessageCounterToContinue" | Defines the next value of the intern message counter that will be sent. Applicable for the PGNs 0, 1024, 2816, 61469 and 61483 only (see Message Checksum and Message Counter). Valid values for propertyValue are 0 to 7 (PGN = 0) or 0 to 15 (all other applicable PGNs). |
| propertyValue | New value to be set for the property |

## Example

```c
if (Iso11783IL_SetMessageProperty(TSC1, "MessageCounterToContinue", 12) < 0)
{
  write("Can’t set message property ‘MessageCounterToContinue‘");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
