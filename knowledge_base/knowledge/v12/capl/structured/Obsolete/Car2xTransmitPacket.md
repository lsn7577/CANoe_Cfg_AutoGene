# Car2xTransmitPacket

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long C2xTransmitPacket( char *message, char *onC2xTransmitPacket)
```

## Description

Registers a CAPL callback function that is invoked before transmission of a database defined packet. This allows the modification of signals and stack values before a packet is sent.

The callback must have the following signature:

void <OnC2xTransmitPacket> ( long packet )

## Return Values

0 or error code

## Example

```c
on start
{
  C2xTransmitPacket("BasicSafetyMessage", "OnTxBSM") ;
}
void OnTxBSM(LONG packet)
{
  C2xSetSignal("BasicSafetyMessage::blob1::_Blob_BSMblob::motion::heading", 90) ;
}
```

## Availability

| Up to Version |
|---|
