# ethClearMacAddressTable

> Category: `IP` | Type: `function`

## Syntax

```c
long ethClearMacAddressTable( long channel);
```

## Description

Clears the MAC address table of the Ethernet network interface.

In channel-based mode the function can only be used with Vector network interface (i.e. VN5640) in operation mode which manages a MAC address table, i.e. Ethernet switch.

In port-based mode the function resets the tables of all switches within the network referenced by the channel number.

## Parameters

| Name | Description |
|---|---|
| channel | Ethernet channel number. Value range: 1..32 |

## Example

```c
on key '1'
{
  EthClearMacAddressTable( 1 ); // clear table on Eth 1
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP3 | 9.0 SP3 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
