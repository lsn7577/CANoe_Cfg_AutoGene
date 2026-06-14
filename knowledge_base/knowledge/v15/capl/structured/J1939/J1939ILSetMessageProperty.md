# J1939ILSetMessageProperty

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILSetMessageProperty( dbMsg msg, char propertyName[], long propertyValue); // form 1
long J1939ILSetMessageProperty(dbNode node, dbMsg msg, char propertyName[], long propertyValue); // form 2
```

## Description

This function sets the internal property of a message.

## Parameters

| Name | Description |
|---|---|
| msg | message name as defined in the database |
| Value | Description |
| "MessageCounterToContinue" | Defines the next value of the intern message counter that will be sent. Applicable for the PGNs 0, 1024, 2816, 61469 and 61483 only (see Message Checksum and Message Counter”). Valid values for propertyValue are 0 to 7 (PGN = 0) or 0 to 15 (all other applicable PGNs). |
| propertyValue | new value to be set for the property |
| node | Simulation node to apply the function |

## Example

```c
if (J1939ILSetMessageProperty(TSC1, "MessageCounterToContinue", 12) < 0)
{
  write("Can’t set message property ‘MessageCounterToContinue‘");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1: form 1 12.0: form 2 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 | J1939 | — | — | form 2 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
