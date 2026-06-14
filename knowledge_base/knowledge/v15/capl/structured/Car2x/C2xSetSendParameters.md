# C2xSetSendParameters

> Category: `Car2x` | Type: `function`

## Syntax

```c
C2xSetSendParameters(LONG appChannel, LONG txPower, LONG antenna, LONG dataRate, LONG expiry)
```

## Description

Set transmission relevant send parameters.

This method allows to redefine some or all transmission related parameters on the fly; for all following transmissions on a specific VN4610 channel those new default values will be used.

In fact the method overwrites the corresponding internal configuration settings provided by the setup-dialog.

To set just a subset of the parameters the value <-1> can be used for antenna, dataRate and expiry to leave the corresponding parameters of the configuration unchanged.

## Parameters

| Name | Description |
|---|---|
| appChannel | Channel to apply settings to (1 .. n), n = available hardware channels (1=Ath1, 2=Ath2,…) |
| txPower | Transmission power in dBm; use -100 to keep the original setting. |
| antenna | Antenna used for Tx: 1: Ant1 2: Ant2 3: both -1: keep the original setting |
| dataRate | Data rate [Mbps] to be used (use 4 to set 4.5Mbps); Allowed values: 3,4,6,9,12,18,24,27 -1: keep the original setting |
| expiry | MAC expiry time [µs] 0: never -1: keep the original setting |

## Example

```c
on key '1'
{
  Write("Set SendParameters for Ch1 to -10dBm  Ant2, 9Mbps; don’t change expiry ");
  C2xSetSendParameters(1, -10, 2, 9, -1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | — | — | — | 3.0 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
