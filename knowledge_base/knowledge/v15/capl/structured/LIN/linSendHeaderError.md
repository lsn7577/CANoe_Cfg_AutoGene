# linSendHeaderError

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSendHeaderError(byte syncByte, byte idWithParity, byte StopAfterError);
```

## Description

This function sends a header with the current sync break, sync delimiter and interbyte space settings and the specified sync byte and id byte.

## Parameters

| Name | Description |
|---|---|
| syncByte | Data value to be sent in the Synch Byte field. Correct value is 0x55 Value range: 0..0xFF |
| idWithParity | Data value to be sent in the Protected Identifier field. The lower 6 bits specify the identifier to be used. The upper 2 bits specify the identifier parity to be used. The correct value can be calculated using the linGetProtectedID function. Value range: 0..0xFF |
| StopAfterError | Specifies whether the transmission should be stopped after an error. If an incorrect synch byte is set by this function and StopAfterError is 1, the identifier will not be sent. A simulated message response (has to be activated independently) will generally not be sent if there is an error in the header. Value range: 0..1 |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// Force an error in header of LIN frame with ID=0x33 by setting wrong protected ID
on key 'h'
{
   byte linID, protectedID, corParity, errParity, errPID;
   // calculate protected ID with wrong parity bits
   linID = 0x33; // use frame ID=0x33
   protectedID = linGetProtectedID(linID); // get protected ID
   corParity = (protectedID & 0xC0) >> 6; // extract parity (0xC=0=11000000)
   errParity = (corParity ^ 0x2) & 0x3; // calculate wrong parity using XOR
   errPID = linID | (errParity << 6); // calculate PID with wrong parity
   linSendHeaderError(0x55, errPID, 0);
}
...
or
...
// Force an error in header of LIN frame with ID=0x33 by setting wrong Synch byte
linSendHeaderError(0x50, linGetProtectedID(0x33), 0);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 SP2 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
