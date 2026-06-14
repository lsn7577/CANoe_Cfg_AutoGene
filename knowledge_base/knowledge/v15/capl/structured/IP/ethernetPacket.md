# ethernetPacket

> Category: `IP` | Type: `function`

## Syntax

```c
ethernetPacket(packet var);
```

## Description

Can be used to create an Ethernet send object. The object data can be manipulated by selectors associated with this object.

## Parameters

| Name | Description |
|---|---|
| packet var | Character string defining the object’s variable name. |

## Example

Example

Example for network-based access

Example for channel-based access

```c
ethernetPacket txPacket;
int i;

txPacket.msgChannel = 1;
txPacket.source      = EthGetMacAddressAsNumber( "20:00:00:00:00:01" );
txPacket.destination = EthGetMacAddressAsNumber( "FF:FF:FF:FF:FF:FF" );
txPacket.Length      = 100;
txPacket.type        = 0xF123;

for( i = 0; i < txPacket.Length; i++ )
{
  txPacket.Byte(i) = i & 0xFF;
}

output( txPacket );
ethernetPacket txPacket;
int i;

txPacket.msgChannel = 1;
txPacket.hwPort = ethernetPort::Ethernet1::ChatClient1;
txPacket.source      = EthGetMacAddressAsNumber( "20:00:00:00:00:01" );
txPacket.destination = EthGetMacAddressAsNumber( "FF:FF:FF:FF:FF:FF" );
txPacket.Length      = 100;
txPacket.type        = 0xF123;

for( i = 0; i < txPacket.Length; i++ )
{
  txPacket.Byte(i) = i & 0xFF;
}

output( txPacket );
ethernetPacket txPacket;
int i;

txPacket.msgChannel  = 1;
txPacket.hwChannel   = 2;
txPacket.source      = EthGetMacAddressAsNumber( "20:00:00:00:00:01" );
txPacket.destination = EthGetMacAddressAsNumber( "FF:FF:FF:FF:FF:FF" );
txPacket.Length      = 100;
txPacket.type        = 0xF123;

for( i = 0; i < txPacket.Length; i++ )
{
  txPacket.Byte(i) = i & 0xFF;
}
output( txPacket );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 9.0 SP3: selector hwChannel 10.0: methods 11.0: selector Simulated 11.0 SP3: protocol selector and methods 12.0 SP4: selector hwPort | 8.5 9.0 SP3: selector hwChannel 10.0: methods 11.0: selector Simulated 11.0 SP3: protocol selector and methods 12.0 SP4: selector hwPort | 13.0 | — | — | 2.0 SP2 2.1 SP3: selector hwChannel 2.2: methods 3.0: selector Simulated 3.0 SP3: protocol selector and methods 5.0: selector hwPort |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
