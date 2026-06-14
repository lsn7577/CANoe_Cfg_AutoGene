# C2xOutputPacket

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xOutputPacket( long packet) // form 1
long C2xOutputPacket( long packet, long txPower ) // form 2
```

## Description

This function sends a WLAN packet. (form 1)

This function sends a WLAN packet with a specific txPower. (form 2)

This method extends the existing OutputPacket function and allows to send a frame with a dedicated Tx-power. It can be used in combination with the existing (old) OutputPacket function, which still uses the default-txPower defined in the Setup-Dialog or by SetSendParameters.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the packet to send |
| txPower | Transmission power in dBm |

## Example

see also example of C2xInitPacket

```c
void SendGNPacket()
{
  long handle;   // handle to c2x message
  long counter = 0, txPower = 25;
  handle = C2xInitPacket("geo_cnh");    // Create a c2x message

  // If nothing went wrong...
  if (handle != 0 && txPower > -20)
  {
    counter++;
    C2xSetTokenInt(handle, "geo_cnh", "reserved", counter);   // Fill the message with the payload
    C2xOutputPacket(handle, txPower);   // transmit packet with decreasing txPower
    txPower--;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6: form 1 11.0: form 1-2 | — | — | — | 2.1 SP3: form 1 3.0: form 1-2 |
| Restricted To | — | Car2x | — | — | — | Car2x |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
