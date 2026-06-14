# _KLine_FastInitPatternReceived

> Category: `KLine` | Type: `function`

## Syntax

```c
_KLine_FastInitPatternReceived(dword TiniL_us, dword TWup_us, int64 timestampTWup)
```

## Description

Called when a fast init pattern has been received.

Called for the following values:

## Parameters

| Name | Description |
|---|---|
| TiniL_us | TiniL time in us. |
| TWup_us | TWup time in us. |
| timestampTWup | End of fast init pattern timestamp |

## Return Values

—

## Example

```c
_KLine_FastInitPatternReceived( dword TiniL_us, dword Twup_us, int64 timestampTwup)
{
   write(FastInitPattern @%.3f received, type %d, TiniL = %d us, Twup = %d us", timestampTwup / cNs2s, type, TiniL_us, Twup_us);
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
