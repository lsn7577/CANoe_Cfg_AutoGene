# coTfsGuarding

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsGuarding( void );
```

## Description

This test checks the life guarding and node guarding functionality of the node.

The life guarding tests are executed with the following parameters:

After that, the node guarding tests with decreasing time tolerances are executed to check the response time. The permissible deviations are 500 ms, 10 ms, 50 ms and 26 ms. To pass the test, all individual test cases must be run through successfully.

## Return Values

Error code

## Example

```c
if (coTfsGuarding() != 1) {
  write( "guarding test failed");
}
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
