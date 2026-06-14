# applPDUILTxPending

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
dword applPDUILTxPending (dword busContext, dword longID, dword shortID, char name[], dword & aPayloadLength, byte data[]);
```

## Description

This callback is optionally being called before the IL sends a PDU to the bus. In this callback it is possible to prevent the sending of the PDU or to change the data of the PDU.

## Return Values

0: sending of the PDU with the supplied info is prevented.

## Example

Use the new fault injection interface to prevent the sending of a PDU.

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

| Since Version |
|---|
