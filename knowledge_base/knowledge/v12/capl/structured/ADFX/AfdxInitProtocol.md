# AfdxInitProtocol

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxInitProtocol( long packet, char protocolDesignator[] ); // form 1
```

## Description

This function initializes the protocol for a packet. If necessary further needed lower protocols are initialized, e.g. IPv4. Already initialized higher protocols are deleted.

## Return Values

0 or error code

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

| Since Version |
|---|
