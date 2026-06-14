# C2xGetChannelConfiguration

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetChannelConfiguration(long appChannel, long radioChannel, long txPower, long maxTxPower, long layout, long dataRate, long bandWidth, long txAntenna, long rxAntenna)
```

## Description

Retrieve the current configuration parameters of a specific hardware channel.

This method allows to readout all relevant channel parameters opposite to C2xConfigureChannel.

## Parameters

| Name | Description |
|---|---|
| appChannel | Channel to apply settings to (1 .. n), n = available hardware channels (1=Ath1, 2=Ath2,…)” |
| radioChannel | Used radio channel (172, 174, 175, 176, 178, 180, 181, 182, 184) |
| txPower | Default transmission power in dBm for ACK / CTS-messages, if not using individual transmission power setting by C2xOutputPacket; use “-100” to keep the original setting. |
| maxTxPower | Maximum transmission power which will not be exceeded even if requested by txPower setting or OutputPacket. Use “-100” to keep the original setting. |
| layout | 0: LPD, 1: EPD protocol |
| dataRate | Data rate [Mbps] to be used (use “4” to set 4.5Mbps); Allowed values: 3,4,6,9,12,18,24,27; -1: keep the original setting |
| bandwidth | Used channel bandwidth (10: 10 MHz; 20: 20Mhz) |
| txAntenna | Antenna used for Tx: 1: Ant1 2: Ant2 3: both -1: keep the original setting Note: If both hardware channels of a VN4610 device are used, the antenna setting cannot be changed during measurement time, use -1 in this case. |
| rxAntenna | Antenna used for Rx: 1: Ant1 2: Ant2 3: both -1: keep the original setting Note: If both hardware channels of a VN4610 device are used, the antenna setting cannot be changed during measurement time, use -1 in this case. |

## Return Values

0 or error code according to the following.

## Example

```c
on key 'g'
{
  long radioChannel, txPower, maxTxPower, layout, dataRate, bandWidth, txAntenna, rxAntenna, i;
  i = C2xGetChannelConfiguration(1, radioChannel, txPower, maxTxPower, layout, dataRate, bandWidth, txAntenna, rxAntenna);
  if (i != 0)
    Write("C2xGetChannelConfiguration 1 failed with err=%d", i);
  else
    Write("ChannelConfig#1: radio:%d layout:%d txPow:%d maxTxPow:%d rate:%d bandWidth:%d txAnt:%d rxAnt:%d",
      radioChannel, layout, txPower, maxTxPower, dataRate, bandWidth, txAntenna, rxAntenna);
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
