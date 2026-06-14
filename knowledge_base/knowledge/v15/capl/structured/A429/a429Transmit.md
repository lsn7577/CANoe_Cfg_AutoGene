# a429Transmit

> Category: `A429` | Type: `function`

## Syntax

```c
long a429Transmit (a429word myA429Word[], dword myNum);
```

## Description

This function triggers the transfer of myNum A429words to the network hardware interface at once. When the mode Simulated bus is used, a built-in simulation layer takes care of the ARINC word.

The following restrictions apply:

Note that the ARINC word selector Gap (see a429SetGap) may be used to adjust the distance between the ARINC words. A single ARINC word is transmitted or updated with output.

Attention: Be aware that the hardware queue size is limited; therefore calling this method rapidly may cause a queue overflow.

## Parameters

| Name | Description |
|---|---|
| myA429word | array of ARINC words |
| myNum | [1...64] number of elements to be sent from myA429word |

## Example

```c
variables
{
  a429Word * myWord[3];
}

on start {
  int i;
  for (i = 0; i < elCount(myWord); i++) {
    myWord[i].msgChannel = 2;
    myWord[i].Id = 64 + i; // create different label numbers
    // send 3 ARINC words with 38.75 and 37.5 us gap
    a429SetGap (myWord[i],
      a429CalcBitLength(myWord[i].msgChannel, 32 - i));
  }
}

on key 's' {
  int i;
  for (i = 0; i < elCount(myWord); i++) {
    myWord[i].byte(1) += 1;
  }
  a429Transmit(myWord, elCount(myWord)); // update
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP2 | 9.0 SP2 | — | — | — | — |
| Restricted To | A429 | A429 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
