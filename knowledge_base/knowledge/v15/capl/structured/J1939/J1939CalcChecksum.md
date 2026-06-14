# J1939CalcChecksum

> Category: `J1939` | Type: `function`

## Syntax

```c
J1939CalcChecksum(pg * msg, char[] calculationMethod, dword & checksum)
```

## Description

Provides the checksum calculation for all PGNs as described in the J1939 Digital Annex. Possible calculation algorithms and message counter alignment is described in J1939 Functional Safety – Messages With Integrated Checksum and Counter.

## Parameters

| Name | Description |
|---|---|
| msg | The parameter group to calculate the checksum for. |
| calculationMethod | Two letters in the form [A-E][a-f] (e.g. Bc) that define the calculation rule and position of the checksum and message counter. |
| checksum | Out parameter where the checksum is stored. |

## Example

```c
on pg *
{
  long err;
  dword checksum;
  switch(this.pgn)
  {
    case 0xF123: //DCDC4OS
      err = J1939CalcChecksum(this, "Aa", checksum);
      if(checksum != this.byte(7) || err != 0)
      {
        write("Checksum error");
      }
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
