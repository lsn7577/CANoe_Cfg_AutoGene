# applPDUILTxPending

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
dword applPDUILTxPending (dword busContext, dword longID, dword shortID, char name[], dword & aPayloadLength, byte data[]);
```

## Description

This callback is optionally being called before the IL sends a PDU to the bus. In this callback it is possible to prevent the sending of the PDU or to change the data of the PDU.

## Parameters

| Name | Description |
|---|---|
| busContext | The context of the simulation bus this PDU will be sent. |
| longID | With the ID you can identify the PDU. |
| shortID | With the ID you can identify the PDU. |
| name | With the name you can identify the PDU. |
| aPayloadLength | The payload length of the PDU to be sent and the length of the data bytes array. |
| data | Data bytes array with the bytes to be sent. The bytes can optionally be changed. |

## Example

Individual calculation of a checksum and a message counter:

```c
dword applPDUILTxPending (dword busContext, dword longID, dword shortID, char name[], dword & aPayloadLength, byte data[])
{
  dword i;
  byte xor;

  /* PDU “PDU_001” contains a XOR checksum in Byte 0. It will
  * be calculated from the other data bytes of the PDU.
  */
  if(strncmp(name, “PDU_001”, elcount(name)) == 0)
  {
    // calculate
    xor = 0x00;
    for(i = 1; i < aPayloadLength; ++i) {
      xor = xor ^ data[i];
    }
    // set the new checksum
    data[0] = xor;
  }

  /* PDU “PDU_002” contains a 4-Bit message counter in
   * the first 4 Bits of Byte 0.
    */
  if(strncmp(name, “PDU_002”, elcount(name)) == 0)
  {
    // get the old value
    i = data[0] & 0x0F;

    // increment
    i++;
    i = i % 16;

    //set the new message counter
    data[0] = i & 0x0F;
  }
  return 1; // don't prevent sending of the PDU
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | 14 | 14 | — | — |
| Restricted To | — | CAN Ethernet FlexRay | CAN Ethernet FlexRay | CAN Ethernet FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
