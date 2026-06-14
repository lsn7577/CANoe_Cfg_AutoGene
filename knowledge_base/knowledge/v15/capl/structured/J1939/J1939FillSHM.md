# J1939FillSHM

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939FillSHM(pg pgSDM, byte sequenceNumber, pg* pgSHM);
```

## Description

This function uses the PGN, addresses, priority and payload of a Safety Data Message (SDM) as well as a sequence number to set the payload, priority and addresses of a Safety Header Message (SHM).

The payload of the SDM consist of following signals (see SAE J1939-76):

## Parameters

| Name | Description |
|---|---|
| pgSDM | The data of SDM is used to fill the SHM. DLC of SDM shall be 8. |
| sequenceNumber | New sequence number of the SHM. |
| pgSHM | SHM message to be filled. DLC of SHM shall be 8. |

## Example

```c
void SendSHM(pg* sdm, byte sequenceNumber)
{
  pg SHM shm;
  long result;
  result = J1939FillSHM(sdm, sequenceNumber, shm);
  if (result < 0)
  {
    write("J1939FillSHM failed with error %i", result);
  }
  else
  {
    output(shm);
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
