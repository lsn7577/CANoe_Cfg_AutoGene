# OnMostStress

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostStress(long mode, long state)
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

## Return Values

—

## Availability

| Since Version |
|---|
