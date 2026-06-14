# J1587GetParameterCount

> Category: `J1587` | Type: `function`

## Syntax

```c
word J1587GetParameterCount(J1587Message msg /*in*/)
```

## Description

Gets the count of J1587 parameters inside a given J1708 message that can be used to further calls to J1587GetParameter().

## Parameters

| Name | Description |
|---|---|
| msg | J1708 message |

## Return Values

number of parameters

## Example

```c
on J1587Message 50 // 50 is Sender MID, can be dbNode name or MID
{
  write ("Number of parameters received: %d", J1587GetParameterCount(this));
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
