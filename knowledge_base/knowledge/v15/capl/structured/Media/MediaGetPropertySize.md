# MediaGetPropertySize

> Category: `Media` | Type: `function`

## Syntax

```c
long MediaGetPropertySize(dword objHandle, char propertyName[], dword& width, dword& height);
```

## Description

Retrieves a property whose value is a size, expressed as a width and height. Properties can be retrieved on an object specific basis for a media type object (e.g. returned by MediaGetMediaType).

## Parameters

| Name | Description |
|---|---|
| propertyName | Name of the property to be retrieved. For a list of properties that can be retrieved by this function see Media Properties and Major Media Types / Subtypes. |
| objHandle | Media type handle. |
| width | Receives the width. |
| hight | Receives the height. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | 13.0 | — | — | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | — |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | — |
| CANoe System and Communication Setup | N/A | — | ✔ | — | — | — |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | — |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | — |
| 32-Bit | — | ✔ | ✔ | N/A | — | — |
| 64-Bit | — | ✔ | ✔ | — | — | — |
