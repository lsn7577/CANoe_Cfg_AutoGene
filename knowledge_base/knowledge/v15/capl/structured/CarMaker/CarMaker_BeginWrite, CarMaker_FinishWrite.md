# CarMaker_BeginWrite, CarMaker_FinishWrite

> Category: `CarMaker` | Type: `function`

## Syntax

```c
long CarMaker_BeginWrite( );
long CarMaker_FinishWrite( );
```

## Description

Groups several write operations to a single atomic write operation. All write operations succeeding CarMaker_BeginWrite are buffered until the call to CarMaker_FinishWrite.

## Return Values

APO return code

## Example

```c
CarMaker_BeginWrite();
CarMaker_WriteAbs("DM.UserSignal_0", 500, 1.0);
CarMaker_WriteAbs("DM.UserSignal_1", 500, -0.3);
CarMaker_FinishWrite();
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | CarMaker | — | — | — | CarMaker |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
