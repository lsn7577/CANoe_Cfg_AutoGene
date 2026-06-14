# linResetSlave

> Category: `LIN` | Type: `function`

## Syntax

```c
long linResetSlave (); // form 1
long linResetSlave(dword resetToLastConfiguration); // form 2
```

## Description

This function resets the NAD (Node Address for Diagnostic) of the modeled Slave node and marks all its protected identifiers as invalid or it will load the last saved configuration if resetToLastConfiguration is set.

See Notes to the way initial NAD is determined to understand how initial NAD is determined in CANoe.

## Parameters

| Name | Description |
|---|---|
| resetToLastConfiguration | 0: perform a complete reset non-zero: load last saved configuration |

## Return Values

On success this function returns a value unequal to -1, otherwise -1.

## Example

Force Slave reset on a keyboard event

```c
on key 'r'
{
if ( linResetSlave() != -1) {
// from now on the Slave node stops publishing responses 
...
}
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | — | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
