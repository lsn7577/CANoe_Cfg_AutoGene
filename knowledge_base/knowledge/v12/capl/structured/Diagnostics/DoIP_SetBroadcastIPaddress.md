# DoIP_SetBroadcastIPaddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetBroadcastIPaddress(char broadcastAddress[]);
```

## Description

Sets target IP address for broadcast messages sent from this node.

## Return Values

—

## Example

```c
DoIP_SetLocalIPaddress( "192.168.1.123”);
if( sendDirectedBroadcast)
  DoIP_SetBroadcastIPaddress( ""); // send to 192.168.1.255
else if( sendToOtherNetwork)
  DoIP_SetBroadcastIPaddress( "192.168.5.255"); // send to 192.168.5.255
else // restore default
  DoIP_SetBroadcastIPaddress( "255.255.255.255"); // limited broadcast
```

## Availability

| Since Version |
|---|
