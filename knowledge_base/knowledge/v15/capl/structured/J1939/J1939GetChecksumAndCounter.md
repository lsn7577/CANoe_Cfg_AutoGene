# J1939GetChecksumAndCounter

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939GetChecksumAndCounter(pg * msg, char[] calculationMethod, dword & checksum, dword & counter)
```

## Description

This function returns the checksum and the message counter of the given parameter group. The available calculation methods are described in J1939 Functional Safety – Messages With Integrated Checksum and Counter and are used to determine the alignment of the checksum and message counter in the given parameter group. After calling this function the parameters checksum and counter contain the values that where transmitted in the message and the return value indicates if an error occurred.

## Parameters

| Name | Description |
|---|---|
| msg | The parameter group to get the checksum and counter from. |
| calculationMethod | Two letters in the form [A-E][a-f] (e.g. Bc) that define the calculation rule and position of the checksum and message counter. |
| checksum | The checksum retrieved from the given parameter group. |
| counter | The message counter retrieved from the given parameter group. |

## Example

```c
on pg *
{
  long err;
  dword checksum;
  dword counter;
  switch(this.pgn)
  {
    case 0xF123: //DCDC4OS
      err = J1939GetChecksumAndCounter (this, "Aa", checksum, counter);
      if(err != 0)
      {
        write("Invalid calculation method");
      }
      write("Checksum: %d", checksum);
      write("Message Counter: %d", counter);
      break;
    default:
      break;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 15 | 15 | 15 | — | — | 6 |
| Restricted To | J1939 | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
