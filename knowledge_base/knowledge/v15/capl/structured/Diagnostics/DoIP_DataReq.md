# DoIP_DataReq

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_DataReq( byte buffer[], dword count, dword vehicleAddress, dword testerAddress);
```

## Description

Request the transfer of the given data to the DoIP peer.

## Parameters

| Name | Description |
|---|---|
| buffer | Buffer containing the data to be transmitted. |
| count | Size of data in bytes. |
| vehicleAddress | Logical DoIP address of the ECU, i.e. the target in a tester and the source in an ECU simulation. |
| testerAddress | An ECU simulation may specify the logical address of the tester to send to by giving a value other than 0 here. Otherwise and in tester nodes, 0 should be given. This will determine the tester’s address automatically, i.e. the configured value in a tester, or the sender address of the last request in an ECU simulation. |

## Return Values

—

## Example

```c
_Diag_DataRequest( BYTE data[], DWORD count,
                   long furtherSegments)
{
   // send data via DoIP
   DoIP_DataReq( data, count, gDoIPAddress, 0);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 SP4 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
