# TestWaitForJ1939PG

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForJ1939PG (dbMsg aMessage, dword aTimeout);
long TestWaitForJ1939PG (dword aPGN, dword aTimeout);
long TestWaitForJ1939PG (dword aPGN, dword aSourceAddress, dword aDestinationAddress, dword aTimeout);
```

## Description

Waits for the occurrence of the specified message aMessage. Should the message not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| aMessage | Message that should be awaited. Must be a J1939 parameter group. |
| aPGN | Parameter Group Number (with data page) of the message that should be awaited. |
| aSourceAddress | Source address of the message that should be awaited or 0xFFFFFFFF if source address is ignored. |
| aDestinationAddress | Destination address of the message that should be awaited or 0xFFFFFFFF if destination address is ignored. |
| aTimeout | Maximum time that should be waited [ms](Transmission of 0: no timeout controlling). |

## Example

```c
long result;
//wait for RQST PG (sent form SA=0x01 to DA=0xAA) for 2000 ms
result = TestWaitForJ1939PG(0xEA00, 0x01, 0xAA, 2000);
if (result == 1)
{
  pg RQST pgRQST; //PG RQST has to be defined in the attached DBC file
  if (TestGetWaitJ1939PGData(pgRQST) == 0)// obtain the received RQST PG
  {
    if (pgRQST.ParameterGroupNumber == 0x1234) //check content of the received PG
    {
      // do something, e.g. send response...
    }
  }
  else
  {
    write("Failed to get data of received PG RQST");
  }
}
else if(result == 0)
{
  write("Expected PG RQST is not received during 2000 ms", result);
}
else
{
  write("TestWaitForJ1939PG(0xEA00, 0x01, 0xAA, 2000): unexpecetd error %i", result);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP3 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
