# coTfsODChk

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsODChk( void );
```

## Description

This function executes an user defined object dictionary test.

Test preparation

The objects which are to test should be added to the internal list of the test objects with the following functions:

With the function coTfsODSetErrorHandling the behavior in an error case can be defined.

Test flow

The function checks every object dictionary entry of existence and size. Additionally the value is compared with the given value. The compare mask defines which data bits are compared and musts be identical.

The complete test is only executed if the access type of the object is not writeOnly.

On a positive comparison and access type readWrite, the read value is written also.

Test result

The test was successful if all necessary objects exist and the read values are identical with the fined values. For optional objects, the test node must answer with a SDO abort code (0x08000000, 0x06020000 or 0x06090011) or return a correct value.

If the access type of the object is readWrite, the read value must be writable with a SDO download without error.

## Return Values

Error code

## Example

```c
see example of coTfsODAddEntry
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
