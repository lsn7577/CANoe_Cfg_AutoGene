# linSendVariableBitStream

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSendVariableBitStream(byte dataBuffer[], int64 lengthInNS[], dword numberOfBits, dword roundUp); // form 1
long linSendVariableBitStream(byte dataBuffer[], int64 lengthInNS[], dword numberOfBits, dword roundUp, dword timeoutPrevention) // form 2
```

## Description

Sends an arbitrary bit stream with bits of variable length on the LIN bus.

## Parameters

| Name | Description |
|---|---|
| dataBuffer | The bit stream to be sent. Maximum number of bits: 2^31-1. |
| lengthInNS | The length of each bit in nanoseconds. |
| numberOfBits | The number of bits in the bitStream-array. Note that while the dataBuffer-array will usually have a size of ceil(numberOfBits / 8), the size of lengthInNS will need to be at least numberOfBits |
| roundUp | If true, the lengths specified in lengthInNS will be rounded up to the next possible length that can be transmitted by the LIN hardware, otherwise the lengths will be rounded down. |
| timeoutPrevention | 0: deactivates the timeout prevention for the 7259-transceiver. 1: activates the timeout prevention for the 7259-transceiver. |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// This function sends a disturbance of 1 second, followed by a pause of 1 second,
// followed by a disturbance of 7 seconds using the variable bit stream functionality
void SendDisturbances()
{
byte data[1] = { 2 };
int64 lengthInNS[3] = { 1000000000LL, 1000000000LL, 7000000000LL };
linSendVariableBitStream(data, lengthInNS, 3, 1, 1);  byte data[25];
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 SP3 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
