# GBT27930IL_SetNodeProperty

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SetNodeProperty( char propertyName[], long propertyValue); // form 1
```

## Description

Changes an internal property of the node.

## Parameters

| Name | Description |
|---|---|
| Property Value | Description Value Range Initial Value |
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

## Example

```c
If(GBT27930IL_SetNodeProperty(„BAM_DT_Interval“, 100) < 0)
{
  write( "Can’t set node property ‘BAM_DT_Interval‘ " );
}
```

## Availability

| Since Version |
|---|
