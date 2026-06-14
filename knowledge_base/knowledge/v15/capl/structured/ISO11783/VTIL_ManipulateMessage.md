# VTIL_ManipulateMessage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ManipulateMessage( dword pgn, dword destinationAddress, qword filterMask, qword filterValue, qword dataMask, qword dataValue ); // form 1
long VTIL_ManipulateMessage( dbNode node, dword pgn, dword destinationAddress, qword filterMask, qword filterValue, qword dataMask, qword dataValue ); // form 2
```

## Description

Modifies the content of a message generated and sent by the interaction layer.

The message to manipulate is specified by PGN, destination address and a part of the first eight data bytes.

To revert this command you can use VTIL_ResetManipulatedMessage or VTIL_ResetAllManipulatedMessages.

## Parameters

| Name | Description |
|---|---|
| pgn | The message with this PGN shall be modified. |
| destinationAddress | 0 - 255: The message which is sent to this address shall be modified. 0xFFFFFFFF (-1): The destination address of the message doesn’t matter |
| filterMask | Defines the bits of the message which shall be used to identify the message. |
| filterValue | Defines the value of the bits of the message which shall be used to identify the message. If the value of the masked bits of a sent message is equal to this value then the data of the message is modified. |
| dataMask | Defines the bits of the message data which are modified. |
| dataValue | Defines the value of the bits of the message which are modified. |
| node | Simulation node to apply the function. |

## Example

```c
on key 'a'
{
  QWORD filterMask, filterValue, dataMask, dataValue;

  //Manipulate some messages

  // 1. Manipulate ECUtoVT GetMemory message (VT Function = 0xC0):
  //    'Required memory' (bytes 3 to 5) should be set to 7654 bytes (0x001DE6) instead of 1676 bytes (0x00068C)

  // The filterMask should therefore use Byte 1 (contains 'VT function')
  // and Bytes 3 to 5 (contains 'Required Memory').
  filterMask  = 0x000000FFFFFF00FFll;
  // The filterValue contains the value 'GetMemory'(0xC0)
  // and the memory to be changed (0x00068C) at the corresponding positions.
  filterValue = 0x00000000068C00C0ll;
  // We only change the RequiredMemory value. VT function should not be changed.
  // Therefore, the dataMask contains only the bits that contain the value of'RequiredMemory'.
  dataMask    = 0x000000FFFFFF0000ll;
  // And dataValue contains only the new value (0x001DE6) of the 'RequiredMemory'.
  dataValue   = 0x000000001DE60000ll;
  ISO11783IL_ManipulateMessage(0xE700 /*ECUtoVT*/, 0x26 /*destinationAddress*/,
  filterMask, filterValue, dataMask, dataValue);

  // 2. Manipulate ECUtoVT Working Set Maintenance message (VT Function = 0xFF):
  //    'Version Number' (Byte3) should be set to Version 5 (0x5) instead of Version 4 (0x4)

  // The filterMask should therefore use Byte 1 (contains 'VT function')
  // and Bytes 3(contains 'Version Number').
  filterMask  = 0x0000000000FF00FFll;
  // The filterValue contains the value 'Working Set Maintenance'(0xFF)
  // and the version to be changed (0x4) at the corresponding positions.
  filterValue = 0x00000000000400FFll;
  // We only change the 'Version Number' value. VT function should not be changed.
  // Therefore, the dataMask contains only the bits that contain the value of'Version Number'.
  dataMask    = 0x0000000000FF0000ll;
  // And dataValue contains only the new value (0x001DE6) of the 'RequiredMemory'.
  dataValue   = 0x0000000000050000ll;
  ISO11783IL_ManipulateMessage(0xE700 /*ECUtoVT*/, 0x26 /*destinationAddress*/,
                                filterMask, filterValue, dataMask, dataValue);
}

on key 'b'
{
  QWORD filterMask, filterValue, dataMask, dataValue;

  //Stop the manipulation configured in the previous function

  // 1. Reset the manipulation of ECUtoVT GetMemory message (VT Function = 0xC0)
  //    where the Required memory (bytes 3 to 5) is equal to 1676 bytes (0x00068C)

  // The filterMask should therefore use Byte 1 (contains 'VT function')
  // and Bytes 3 to 5 (contains 'Required Memory').
  filterMask  = 0x000000FFFFFF00FFll;
  // The filterValue contains the value 'GetMemory'(0xC0)
  // and the memory to be changed (0x00068C) at the corresponding positions.
  filterValue = 0x00000000068C00C0ll;
  ISO11783IL_ResetManipulatedMessage(0xE700 /*ECUtoVT*/, 0x26 /*destinationAddress*/, filterMask, filterValue);

  // 2. Reset the manipulating of ECUtoVT Working Set Maintenance message (VT Function = 0xFF)
  //    where 'Version Number' (Byte3) is equal to Version 4 (0x4)

  // The filterMask should therefore use Byte 1 (contains 'VT function')
  // and Bytes 3(contains 'Version Number').
  filterMask  = 0x0000000000FF00FFll;
  // The filterValue contains the value 'Working Set Maintenance'(0xFF)
  // and the version to be changed (0x4) at the corresponding positions.
  filterValue = 0x00000000000400FFll;
  ISO11783IL_ResetManipulatedMessage(0xE700 /*ECUtoVT*/, 0x26 /*destinationAddress*/, filterMask, filterValue);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | 13.0 | — | — | 3.0 SP3 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
