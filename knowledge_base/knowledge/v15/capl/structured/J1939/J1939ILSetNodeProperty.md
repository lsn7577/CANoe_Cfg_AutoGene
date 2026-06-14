# J1939ILSetNodeProperty

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILSetNodeProperty( char propertyName[], long propertyValue); // form 1
long J1939ILSetNodeProperty(dbNode node, char propertyName[], long propertyValue); // form 2
```

## Description

Changes an internal property of the node.

## Parameters

| Name | Description |
|---|---|
| Property Value | Description Value Range Initial Value |
| FP_Interval | Defines delay (im ms) when sending each FP packet (for Fast Packet transmitting). 0..3600000 0 |
| BAM_DT_Interval | Defines the interval time (in millisec) between each TP DT packet (for BAM transmitting). 1..3600000 50 ms |
| CTSLatency | Defines the interval time (in millisec) between the TP.CM_RTS and TP.CM_CTS (for the receiver of the CMDT transmitting). 1..1249 0 ms |
| EoMALatency | Defines the interval time (in millisec) between the last TP.DT and TP.CM_ EndOfMsgACK (for the receiver of the CMDT transmitting). 1..1249 0 ms |
| AbortLatency | Defines delay (in millisec) for sending the TP.Conn_Abort message (for both the sender and the receiver of the CMDT transmission). 1..199 0 ms |
| TPDTLatency | Defines delay (im millisec) when sending each TP.DT message (for the transmitter of the CMDT transmitting). 1..199 0 ms |
| Max_Transport_Size | Maximum number of bytes, which can be transferred. 9..117440505 100 MByte |
| Packets_Per_CTS | Number of packets, which are requested by CTS. 1..255 16 |
| Packets_Per_RTS | Number of packets, which is used with RTS. 1..255 255 |
| Packets_Per_Sequence_Ex | Number of packets, which are requested by ECTS (Extended TP). 1..255 64 |
| BAM_with_Destination | Target address, which is used for BAM. 0: Target address is 0xFF 1: Specific target address is used 0..1 0 |
| Max_Number_Of_Requested_Retransmissions | Maximal number of retransmission that the interaction layer supports. (Retransmission can be requested by the message TP.CM_CTS). 1..100000 2 |
| TP_Priority | Priority used by the transport protocol. 0..7 7 |
| AAC | Arbitrary Address Capable field of J1939 NAME 0..1 Content of the database node attribute NmJ1939AAC |
| IndustryGroup | Industry Group field of J1939 NAME 0..7 Content of the database node attribute NmJ1939IndustryGroup |
| VehicleSystemInstance | Vehicle System Instance field of J1939 NAME 0..15 Content of the database node attribute NmJ1939SystemInstance |
| VehicleSystem | Vehicle System field of J1939 NAME 0..127 Content of the database node attribute NmJ1939System |
| Function | Function field of J1939 NAME 0..255 Content of the database node attribute NmJ1939Function |
| FunctionInstance | Function Instance field of J1939 NAME 0..31 Content of the database node attribute NmJ1939FunctionInstance |
| ECUInstance | ECU Instance field of J1939 NAME 0..7 Content of the database node attribute NmJ1939ECUInstance |
| ManufacturerCode | Manufacturer Code field of J1939 NAME 0..2047 Content of the database node attribute NmJ1939ManufacturerCode |
| IdentityNumber | Identity Number field of J1939 NAME 0..2097151 Content of the database node attribute NmJ1939IdentityNumber |
| AddressClaimSupport | Type of Address Claim support 0: No Address Claim support1: Basic Address Claim support2: Extended Address Claim support 0..2 0 |
| propertyValue | new value for the property |
| node | Simulation node to apply the function |

## Example

```c
If(J1939ILSetNodeProperty(„BAM_DT_Interval“, 100) < 0)
{
  write( "Can’t set node property ‘BAM_DT_Interval‘ " );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1: form 1 12.0: form 2 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 | J1939 | — | — | form 2 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
