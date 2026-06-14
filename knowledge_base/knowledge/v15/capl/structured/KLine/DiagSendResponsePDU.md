# DiagSendResponsePDU

> Category: `KLine` | Type: `function`

## Syntax

```c
long DiagSendResponsePDU(BYTE rawPDU[], WORD rawPDULength)
```

## Description

Sends a raw byte buffer. E.g. this allows sending responses with invalid protocol headers.

## Parameters

| Name | Description |
|---|---|
| rawPDU | Byte buffer to be transmitted. |
| rawPDULength | Length of the byte buffer. |

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
variables
{
   const cTesterAddress = 0xF1;
   const cEcuAddress = 0x86;
}

_Diag_DataRequest( BYTE data[], dword count, long furtherSegments)
{
   long status;
   // Replace Frame
   BYTE FI_Response[6] = { 0x82, cTesterAddress, cEcuAddress, 0x99, 0xff, 0x01 };
   FI_Response[3] = data[0];
   DiagSendResponsePDU( FI_Response, elcount( FI_Response));
   return;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP4 | — | — | — | 1.1 SP2 |
| Restricted To | — | K-Line Real bus mode Online mode ECU simulation | — | — | — | K-Line Real bus mode Online mode ECU simulation |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
