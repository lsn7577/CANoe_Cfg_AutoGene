# J1939ParseSHM

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ParseSHM(pg* pgSHM, dword & sdmPgn, byte& sdmSourceAddress, byte& sdmDestinationAddress, byte& sequenceNumber, dword & crc):
```

## Description

Provides data of the SDM message, which are contained in payload of the SHM message according to SAE J1939-76.

## Parameters

| Name | Description |
|---|---|
| pgSHM | SHM to parse. DLC of SHM shall be 8. |
| sdmPgn | Returns the PGN of the SDM. |
| sdmSourceAddress | Returns the source address of the SDM. |
| sdmDestinationAddress | Returns the destination address of the SDM. |
| sequenceNumber | Returns the sequence number of the Safety Data Group (SDG). |
| crc | Returns the SDM Data CRC. |

## Example

```c
on pg SHM
{
  long result;
  dword sdmPgn, crc;
  byte sdmSourceAddress, sdmDestinationAddress,sequenceNumber;

  result = J1939ParseSHM(this, sdmPgn, sdmSourceAddress, sdmDestinationAddress, sequenceNumber, crc);
  if (result < 0)
  {
    write("J1939ILParseSHM failed with error %i", result);
  }
  else
  {
    if ((sdmPgn == pgnOfConsumedMsg)
    && (sdmDestinationAddress == saOfConsumedMsg)
    && (sdmSourceAddress      == daOfConsumedMsg))
    {
      // validate sequence number of SHM and store store CRC to validate it when SDM is received
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 15 | 15 | 15 | — | — | 6 |
| Restricted To | J1939 | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
