# coTfsSDOChkEntryExists

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOChkEntryExists( dword index, dword subindex );
```

## Description

This function checks with a SDO upload if the object is readable.

## Parameters

| Name | Description |
|---|---|
| index | Object index in the object dictionary. |
| subindex | Object sub index in the object dictionary. |

## Return Values

Error code or one of the following values

## Example

```c
/* check if object [1000,0] is readable. This function is mainly a SDO upload function, but the test report output differs to make it more useful to check if an optional object exists */
if (coTfsSDOChkEntryExists(0x1000, 0) != 1)
{
  /* entry does not exist, 0x1000 is mandatory, so something serious is wrong here */
} /* if */
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
