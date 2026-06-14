# diagGetObjectName

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetObjectName( diagResponse obj, char nameBufferOut[], dword nameBufferLen);
long diagGetObjectName( diagRequest obj, char nameBufferOut[], dword nameBufferLen);
```

## Description

Writes the language dependent name of the diagnostics object into the buffer. For ODX descriptions, this is the "long name".

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object |
| nameBufferOut | Output buffer |
| nameBufferLen | Output buffer size |

## Return Values

Length of service name written to buffer, may be truncated.
Error code

## Example

```c
DiagRequest AirbaContr_Read req;
char name[100];
DiagGetObjectName( req, name, elcount( name));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 | 5.2 7.0 SP5: methods | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
