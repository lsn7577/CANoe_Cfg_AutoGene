# AfdxInitProtocol

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxInitProtocol( long packet, char protocolDesignator[] ); // form 1
long AfdxInitProtocol( long packet, char protocolDesignator[], char packetTypeDesignator[] ); // form 2
```

## Description

This function initializes the protocol for a packet. If necessary further needed lower protocols are initialized, e.g. IPv4. Already initialized higher protocols are deleted.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket. |
| protocolDesignator | Name of the protocol. |
| packetTypeDesignator | Type of the packet. |

## Example

```c
testfunction Packet_InitProtocolICMP( long expectError, char expectErrorText[] )
{
  //
  // Create AFDX gPacket
  //
  gPacket_Result = AfdxInitProtocol( gPacket[gPacketSelect], "afdx", "icmp" );

  if (expectError == 0)
  {
    if (gPacket_Result != 0)
    {
      snprintf( gPacket_Text, elcount(gPacket_Text), "AfdxInitProtocol failed, result %d", gPacket_Result );
      TestStepFail( gPacket_Text );
      Packet_ReportLastError();
      return;
    }
    else
    {
      TestStepPass();
    }
  }
  else
  {
    if (Packet_CheckExpectError( "AfdxInitProtocol", expectError, expectErrorText ))
    {
      TestStepPass();
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
