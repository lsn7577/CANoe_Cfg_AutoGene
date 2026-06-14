# applILTxPending

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
dword applILTxPending(long aId, dword aDlc, byte data[]);
```

## Description

This callback is optionally being called before the IL sends a message to the bus. In this callback it is possible to prevent the sending of the message or to change the data of the message.

## Parameters

| Name | Description |
|---|---|
| aId | With the ID you can identify the message. |
| aDLC | The DLC of the message to be sent and the length of the data bytes array. |
| data | Data bytes array with the bytes to be sent. The bytes can optionally be changed. |

## Example

Calculation of a checksum and a message counter:

```c
dword applILTxPending (long aId, dword aDlc, byte data[])
{
  dword i;
  byte xor;
  /* Message 0x1A0 contains a XOR checksum in Byte 0. It will
  /* be calculated from the other data bytes of the message.
  */
  if(aId == 0x1A0)
  {
    // calculate
    xor = 0x00;
    for(i = 1; i < aDlc; ++i) {
      xor = xor ^ data[i];
    }
    // set the new checksum
    data[0] = xor;
  }
  /* Message 0x1A1 contains a 4-Bit message counter in
  /* the first 4 Bits of Byte 0.
  */
  if(aId == 0x1A1)
  {
    // get the old value
    i = data[0] & 0x0F;
    // increment
    i++;
    i = i % 16;
    //set the new message counter
    data[0] = i & 0x0F;
  }
  return 1; // don't prevent sending of the message
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP2 | 14 | 14 | — | — |
| Restricted To | — | CAN | CAN | CAN | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
