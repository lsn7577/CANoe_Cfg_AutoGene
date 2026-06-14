# linInvertHeaderBitEx

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linInvertHeaderBitEx(dword byteIndex, dword bitIndex, dword bitOffsetInSixteenthBits, dword distLengthInSixteenthBits, dword level); // form 1
dword linInvertHeaderBitEx(dword byteIndex, dword bitIndex, dword bitOffsetInSixteenthBits, dword distLengthInSixteenthBits, dword level, dword numberOfExecutions, dword reportFallingEdges); // form 2
dword linInvertHeaderBitEx(dword byteIndex, dword bitIndex, dword bitOffsetInSixteenthBits, dword distLengthInSixteenthBits, dword level, dword numberOfExecutions, dword reportFallingEdges, long disturbAfterHeaderID, dword waitForHeaders); // form 3
```

## Description

Inverts the specified number of 1/16th bits at the specified position in the next LIN header.

## Parameters

| Name | Description |
|---|---|
| byteIndex | Index of the byte. -1: Sync Break 0: Sync Byte 1: ProtectedId Byte |
| bitIndex | The index of the bit to be manipulated. An index in the range 0-7 will manipulate a data bit, while the index 8 will manipulate the stop bit. Higher index values will cause the interbyte-space after the data byte to be manipulated. In this case, the user should make sure that the interbyte-space is large enough. Since the bit index is based on a UART-byte, index 0 will not disturb the very first bit (i.e. the start bit) but the first data bit. Note that it is technically impossible to disturb the first bit of a dominant signal since by the time the falling edge has been seen, it is already to late to disturb that bit (i.e. you cannot undo the falling edge). This type of indexing means that in order to disturb the first bit in the sync delimiter you have to use the index <length of sync break> - 1. I.e. in case of an 18 bit break, index 17 will disturb the first bit in the sync delimiter. Value range: 0..255 |
| bitOffsetInSixteenthBits | The offset in 1/16th bits into the bit specified in bitIndex. Value range: 0..15 |
| distLengthInSixteenthBits | The length of the disturbance in units of 1/16th bit. Value range: 0..65535 |
| Level | Level of the disturbance. 0: Dominant (inverts recessive bit) 1: Recessive (inverts dominant bit – requires mag-Cab/Piggyback and external power supply) |
| numberOfExecutions | The number of consecutive headers in which the bit inversion will be executed. Default: 1 (single shot).The largest possible value is 255. If a larger value is given, 255 will be used. |
| reportFallingEdges | Flag indicating whether time stamps of the falling edges in the resulting pseudo-byte have to be reported. The time stamps can be retrieved by calling linGetFallingEdgesOfDisturbedByte. 0: Deactivate report |
| disturbAfterHeaderID | With this parameter and the next one it is possible to define exactly which header will be disturbed. The LIN hardware will first wait for a header with ID = disturbAfterHeaderID before additionally awaiting the number of headers defined by waitForHeaders. The next header following these headers will then be disturbed. For example: To disturb the next header directly after a header with the ID=5, set the disturbAfterHeaderID parameter to 5 and the waitForHeaders to 0. |
| waitForHeaders | See explanation for disturbAfterHeaderID. |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 'i'
{
   if (0!=linInvertHeaderBitEx(0, 0, 8, 8, 0))
   {
   // for the next LIN header invert the second half of the first bit (it’s the recessive one) of the Sync byte
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 SP2: form 1-2 7.5: form 3 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
