# J1939SetChecksumAndCounter

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939SetChecksumAndCounter(pg * msg, char[] calculationMethod, dword counter)
```

## Description

This function calculates and sets the checksum of the given parameter group as well as the given counter. The available calculation algorithms are described in J1939 Functional Safety – Messages With Integrated Checksum and Counter.

## Parameters

| Name | Description |
|---|---|
| msg | The parameter group to calculate and set the checksum for. |
| calculationMethod | Two letters in the form [A-E][a-f] (e.g. “Bc”) that define the calculation rule and position of the checksum and message counter. |
| counter | Current message counter to be set in the given parameter group. |

## Example

```c
on key 'a'
{
  long err;
  pg * msg;
  dword counter = 0;

  msg.PGN = 0xF123; //DCDC4OS
  msg.SA = 0x1;
  msg.dlc = 8;
  msg.byte(0) = 0x01;
  msg.byte(1) = 0x02;
  msg.byte(2) = 0x03;
  msg.byte(3) = 0x04;
  msg.byte(4) = 0x05;
  msg.byte(5) = 0x06;
  msg.byte(6) = 0x07; // Bits 4-8 will be overwritten with the message counter
  msg.byte(7) = 0x08; // Will be overwritten with the checksum

  if(J1939SetChecksumAndCounter(msg, "Aa", counter) != 0)
  {
    write("Error while setting checksum and counter");
  }
  counter = (counter + 1) % 16;
  output(msg);
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
