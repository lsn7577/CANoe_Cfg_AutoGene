# ethGetLinkStatus

> Category: `IP` | Type: `function`

## Syntax

```c
long ethGetLinkStatus( long channel ); // form 1
```

## Description

Returns the link status of the channel.

## Return Values

0: Link down

## Example

```c
on key 'i'
{
  write("Link status has the value: %d", ethGetLinkStatus(ethernetPort::MyNetworkName::MyPortName));
}
```

## Availability

| Since Version |
|---|
