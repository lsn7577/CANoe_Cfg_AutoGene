# ReadByteArraySignalAsInteger

> Category: `SignalAccess` | Type: `function`

## Syntax

```c
dword ReadByteArraySignalAsInteger(signal aSignal, qword& value, dword direction, dword byteOrder, dword byteFillMode) // form 1
dword ReadByteArraySignalAsInteger(pdu aPDU, char signalName[], qword& value, dword byteOrder, dword byteFillMode) // form 2
```

## Description

Reads the value of a byte array signal and treats it as a 64-bit integer. Use this function if you previously read the value of a byte array signal with the .raw64 selector. This selector works only for integer signals, but byte array signals were treated incorrectly as integer signals in CANoe versions < 12.0 SP3.

## Parameters

| Name | Description |
|---|---|
| aSignal | A byte array signal |
| aPDU | An AUTOSAR PDU with a byte array signal |
| signalName | Name of the signal on the PDU |
| value | The read value (out parameter) |
| direction | Whether the rx signal (parameter value 0) or the tx signal value buffer (parameter value 1) shall be read. |
| byteOrder | Byte order for interpreting the signal bytes. 0: little-endian (intel) 1: big-endian (motorola) See examples below. |
| byteFillMode | How the remaining bits of the 64-bit integer shall be filled if the signal has less than 64 bits. 0 means add 0 bits before the signal bits. 1: sign-extend. Add 0 or 1 bits before the signal bits, depending on the first signal bit. 2: Add 0 bits after the signal bits (effectively a right-shift of the value). See examples below. |

## Example

If a signal has 56 bits (7 bytes) and the value shall be interpreted in motorola (big-endian) byte order, depending on the byteFillMode parameter, the following value will be read if the bytes of the signal are "91 23 45 67 89 AB CD":

If the value shall be interpreted in intel (little-endian) byte order, depending on the byteFillMode parameter, the following value will be read if the bytes of the signal are "EF CD AB 89 67 45 23":

```c
byteFillMode == 0: value == 0x009123456789ABCD // prepend 0s
byteFillMode == 1: value == 0xFF9123456789ABCD // sign-extension
byteFillMode == 2: value == 0x9123456789abcd00 // append 0s
byteFillMode == 0: value == 0x0023456789ABCDEF // prepend 0s
byteFillMode == 1: value == 0x0023456789ABCDEF // sign-extension
byteFillMode == 2: value == 0x23456789ABCDEF00 // append 0s
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | 14 | — | — | 5.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
