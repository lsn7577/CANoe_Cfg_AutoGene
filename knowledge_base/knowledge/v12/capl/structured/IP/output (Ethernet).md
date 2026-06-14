# output (Ethernet)

> Category: `IP` | Type: `function`

## Syntax

```c
void output(ethernetPacket packet); // form 1
```

## Description

Outputs an Ethernet packet (form 1) from the program block.Form 2 can be used to output Ethernet packets with an invalid frame checksum.

## Return Values

—

## Example

```c
ethernetPacket txPacket;

txPacket.msgChannel = 1;
txPacket.source      = EthGetMacAddressAsNumber( "20:00:00:00:00:01" );
txPacket.destination = EthGetMacAddressAsNumber( "FF:FF:FF:FF:FF:FF" );
txPacket.Length = 100;
txPacket.type = 0xF123;

output( txPacket, 0x1234 );
```

## Availability

| Since Version |
|---|
