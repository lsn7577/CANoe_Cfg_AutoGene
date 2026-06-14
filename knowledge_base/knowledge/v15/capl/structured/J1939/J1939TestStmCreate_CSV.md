# J1939TestStmCreate_CSV

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestStmCreate_CSV( pg aPg, dbSignal aSignal, dword cycleTime, char csvFile[] );
```

## Description

Creates a CSV Stimulus. The values for the Stimulus are loaded from a CSV file.

## Parameters

| Name | Description |
|---|---|
| aPg | This parameter group is used for sending. If no sender or receiver is specified, the addresses from this PG is used. The signal of the PG can be modified during active Stimulus. |
| aSignal | The Stimulus works on this signal of the parameter group. |
| cycleTime | cycle time in milliseconds |
| csvFile | filename of the CSV file, CANoe loads this file from the configuration directory |

## Example

```c
long csvStm;
pg MyPG myPG;

myPG.SA = 1;
myPG.DA = 2;

csvStm = J1939TestStmCreate_CSV( myPG, MyPg::SignalA, 100, "Values.csv" );
J1939TestStmControl_Start(csvStm);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
