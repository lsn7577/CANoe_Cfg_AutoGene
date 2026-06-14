# linGetDlc

> Category: `LIN` | Type: `function`

## Syntax

```c
long linGetDlc(long frameID);
```

## Description

Queries the Data Length Code (i.e. length in bytes) of a LIN frame.

Per default the DLC of LIN frames is initialized according to the LIN Description File (LDF).

If no LDF is used, this function returns the DLC initialized in on preStart e.g. using linSetDlc, for LIN frames sent by simulated LIN nodes.

For LIN frames whose DLC has not been initialized, this function will return the default DLC for the selected ID as defined in the LIN1.1 protocol specification.

For LIN frames sent by external LIN nodes, the measured DLC is returned.

## Parameters

| Name | Description |
|---|---|
| frameID | LIN frame identifier in the range 0 .. 63. |

## Return Values

If successful the frame length [in bytes] or -1 on failure.

## Example

Verify correct DLC is used by a certain frame

```c
...
if ( linGetDLC(0x22) != 5)
{
linChangeDLC(0x22, 5); // set DLC of frame with identifier 0x22 to be 5
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.1 | 3.1 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
