# coTfsGetVersion

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword coTfsGetVersion( void );
```

## Description

This function returns the internal version number of this CANopen Test Feature Set node layer.

## Return Values

Version number

## Example

```c
dword majorVersion;
dword minorVersion;

minorVersion = coTfsGetVersion();
majorVersion = (minorVersion >> 8) & 0xFF;
minorVersion = minorVersion & 0xFF;

write("coTfs node layer version = %d.%d",majorVersion, minorVersion);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
