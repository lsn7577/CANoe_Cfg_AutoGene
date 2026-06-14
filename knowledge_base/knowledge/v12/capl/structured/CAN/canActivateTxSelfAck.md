# canActivateTxSelfAck

> Category: `CAN` | Type: `function`

## Syntax

```c
int canActivateTxSelfAck (int channel, int activate);
```

## Description

Activates/deactivates the transmit self ack feature in CANoe for the defined channel.

## Return Values

0 = device does not support self ack

## Example

```c
on key a'
{
  int channel
  int activate;
  // Activate TX Self-ACK for CAN channel 1
  channel = 1;
  activate = 1;
  canActivateTXSelfAck(channel, activate);
}
```

## Availability

| Since Version |
|---|
