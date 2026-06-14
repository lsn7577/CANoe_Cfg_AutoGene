# ethSetLinkStatus

> Category: `IP` | Type: `function`

## Syntax

```c
long ethSetLinkStatus( long channel, long status ); // form 1
```

## Description

Configures the channel of the Vector hardware to establish or terminate a link.

## Return Values

0: Success

## Example

```c
on key 'u'
{
  ethSetLinkStatus(ethernetPort::MyNetworkName::MyPortName, 1);
}
```

## Availability

| Since Version |
|---|
