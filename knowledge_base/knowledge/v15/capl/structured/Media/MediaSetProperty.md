# MediaSetProperty

> Category: `Media` | Type: `function`

## Syntax

```c
long MediaSetProperty(dword objHandle, char propertyName[], dword value); // form 1
long MediaSetProperty(dword objHandle, char propertyName[], dword length, char value[]); // form 2
long MediaSetProperty(dword objHandle, char propertyName[], qword value); // form 3
long MediaSetProperty(dword objHandle, char propertyName[], dword length, byte value[]); // form 4
```

## Description

The behavior of an object can be configured using properties.

Properties can be set on an object specific basis for a media type object (e.g. returned by MediaGetMediaType).

## Parameters

| Name | Description |
|---|---|
| propertyName | Name of the property to be set. For a list of properties that can be set by this function see Media Properties and Major Media Types / Subtypes. |
| objHandle | Media type handle. |
| length (string overload only) | Length of the value buffer passed. |
| value | New value of the property. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5: from 1, 2: form 1 10.0: from 3, 4: form 1 | 13.0 | — | — | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | — |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | — |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | — |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | — |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | — |
| 32-Bit | — | ✔ | ✔ | N/A | — | — |
| 64-Bit | — | ✔ | ✔ | — | — | — |
