# Crc_CalculateCRC32

> Category: `Other` | Type: `function`

## Syntax

```c
long Crc_CalculateCRC32 (BYTE* data, dword dataSize, dword dataOffset, dword crcLength, dword crcStartValue, dword firstCall, dword* crcCalculated);
```

## Description

Calculates the corresponding checksum for CRC32 based on the data. The calculation of the CRC value corresponds to IEEE-802.3 CRC32.

## Parameters

| Name | Description |
|---|---|
| data | Payload data for which the checksum is to be calculated. |
| dataSize | Length of data block to be calculated in bytes. |
| dataOffset | Start index for the calculation of the CRC in the payload data. |
| crcLength | The length of the data for the CRC is calculated. |
| crcStartValue | CRC initial value depending on whether it is the first call or a subsequent call. Value is ignored if firstCall is 1. |
| firstCall | Flag for first call or a subsequent call. Possible values are 0 (subsequent call) or 1 (first call). |
| crcCalculated | Calculated CRC32 value. |

## Example

```c
// first CALL, Offset '0'
on key 'a'
{
  long  retval;
  dword crc;
  byte  data[9] = {0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39};

  retval = Crc_CalculateCRC32(data, elcount (data), 0, elcount (data), 0, 1, crc);
  write("CRC of data: 0x%X", crc);
}

// first CALL, Offset '2', Length - 2
on key 'b'
{
  long  retval;
  dword crc;
  byte  data[11] = {0xAA ,0xAA,0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39};

  retval = Crc_CalculateCRC32(data, elcount (data), 2, elcount (data) -2, 0, 1, crc);
  write("CRC of data: 0x%X", crc);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP5 | 13.0 | — | 14 | 5.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
