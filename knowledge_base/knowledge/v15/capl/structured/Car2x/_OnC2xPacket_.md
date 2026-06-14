# <OnC2xPacket>

> Category: `Car2x` | Type: `function`

## Syntax

```c
void <OnC2xPacket>( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet );
```

## Description

This callback is called when a registered WLAN packet is received.

Within this callback the following functions can be used to retrieve the received packet data:

This functions access the payload of the highest interpretable protocol. Offset 0 starts at the beginning of the payload.

## Parameters

| Name | Description |
|---|---|
| channel | WLAN channel on which the packet was received |
| dir | Direction of the packet 0: Rx 1: Tx |
| radioChannel | Radio channel, i.e. 176 or 180 |
| signalStrength | Signal strength of the received packet in [dBm] |
| signalQuality | Signal quality of the received packet |
| packet | Handle of the received packet |

## Return Values

—

## Example

Node System - PreStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  C2xReceivePacket( "OnC2xPacket");
}
void <OnC2xPacket>( long channel, long dir, long radioChannel, long signalStrength, long signalQuality, long packet )
{
  byte rx_data[100];
  long rx_length;
  // get the payload of the packet
  rx_length = C2xGetThisData( 0, elCount(rx_data), rx_data );
  // do something with rx_data
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 | — | — | — | 2.1 SP3 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
