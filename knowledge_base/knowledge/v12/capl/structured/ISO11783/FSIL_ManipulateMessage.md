# FSIL_ManipulateMessage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_ManipulateMessage( dword pgn, dword destinationAddress, qword filterMask, qword filterValue, qword dataMask, qword dataValue ); // form 1
```

## Description

Modifies the content of a message generated and sent by the interaction layer.

The message to manipulate is specified by PGN, destination address and a part of the first eight data bytes.

To revert this command you can use FSIL_ResetManipulatedMessage or FSIL_ResetAllManipulatedMessages.

## Return Values

0: Manipulation is set successfully

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

| Since Version |
|---|
