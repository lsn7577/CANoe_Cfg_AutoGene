# TestSetEcuOnline

> Category: `Test` | Type: `function`

## Syntax

```c
void testSetEcuOnline (dbNode aNode);
void testSetEcuOnline (char aNodeName[]);
```

## Description

Connects the ECU to the bus.After calling the testSetEcuOffline() function the ECU can be reconnected to the bus by using the testSetEcuOnline() function. Messages being sent by the ECU will be forwarded to the bus.

This function interferes with the CAPL program and possible Nodelayer DLLs.

## Parameters

| Name | Description |
|---|---|
| aNode | ECU to be switched online (must be defined in the database). |
| aNodeName | Name of the ECU to be switched online (must be defined in the database). Node name can optionally specified by an additional qualifier: NodeName BusName::NodeName |

## Return Values

—

## Example

```c
// cuts the node ‚SUT’ 5000 ms from the bus
TestSetEcuOffline(SUT);
TestWaitForTimeout(5000);
TestSetEcuOnline(SUT)
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
