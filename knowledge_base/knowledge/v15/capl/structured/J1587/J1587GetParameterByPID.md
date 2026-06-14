# J1587GetParameterByPID

> Category: `J1587` | Type: `function`

## Syntax

```c
byte J1587GetParameterByPID(J1587Message msg /*in*/, J1587Param param /*out*/, dword dbPID /*in*/)
```

## Description

Gets a J1587 parameter inside a J1708 message given a specific PID.

The function returns an error if a parameter with the specified dbPID is not found inside the J1708 message.

## Parameters

| Name | Description |
|---|---|
| msg | J1708 message |
| param | returned parameter at the given index |
| dbPID | database PID |

## Return Values

0 or error code

## Example

```c
on J1587Message 50 // 50 is Sender MID, can be dbNode name or MID
{
  dword count, i;
  J1587Param param;

  if (J1587GetParameterByPID(this, param, 80) == 0)
  {
    write ("Parameter with PID 80 received.");
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 | 7.0 | 13.0 | — | — | — |
| Restricted To | J1587 | J1587 | J1587 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
