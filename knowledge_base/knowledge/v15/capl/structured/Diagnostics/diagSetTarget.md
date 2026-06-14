# diagSetTarget

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetTarget (char ecuName[])
```

## Description

Sets the target ECU with which the tester shall communicate from now on and configures/establishes the communication channel to that ECU.

After calling the function in the tester, the following actions are executed:

## Parameters

| Name | Description |
|---|---|
| ecuName | Qualifier of the ECU as set in the diagnostic configuration dialog for the respective diagnostic description (CDD/ODX). |

## Return Values

Error code

## Example

```c
// In this example, diagSetTarget(<ECU>) is simply called once in the
// ‘MainTest’ function of a test node, as this tester only needs to access
// one dedicated ECU with ECU qualifier "Door".
// In case a test module needs to perform diagnostics with different ECUs,
// the function could be called e.g. in the first / initializing test case
// of a test group for each specific ECU

void MainTest ()
{
  if( 0 != diagSetTarget( "Door")) write( "Error setting target!");
  // ... Call your test cases here
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 5.0 | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
