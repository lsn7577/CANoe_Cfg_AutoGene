# OnMostStress

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostStress(long mode, long state);
```

## Description

The event procedure OnMostStress() will be called before the beginning and after the end of the stress generation.

## Parameters

| Name | Description |
|---|---|
| 1 | Stress generation with mostGenerateLightError |
| 2 | Stress generation with mostGenerateLockError |
| 3 | Stress generation with mostGenerateBusloadCtrl |
| 4 | Stress generation with mostGenerateBusloadAsync |
| 5 | Stress generation with mostSetRxBufferCtrl |
| 6 | Stress generation with mostSetTxLightPower |
| 7 | mostGenerateBypassToggle |
| 8 | mostSetSystemLockFlagUsage |
| 9 | mostSetShutDownFlagUsage |
| 10 | mostGenerateBusloadEthPkt |
| 11 | mostSetRxBufferAsync |
| 0 | Stress mode is stopped Note: mode = 5: Rx buffer enabled mode = 6: normal light intensity |
| 1 | Stress mode is started Note: mode = 5: Rx buffer disabled mode = 6: 3db attenuation |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
