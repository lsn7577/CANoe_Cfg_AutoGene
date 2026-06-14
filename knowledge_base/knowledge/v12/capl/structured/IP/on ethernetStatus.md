# on ethernetStatus

> Category: `IP` | Type: `event`

## Syntax

```c
on ethernetStatus *;
```

## Description

The event procedure is called on the change of the status of the Ethernet link.

To access the control information you would use selectors.

The key word this is available within an on ethernetStatus procedure, to access the information of the link status.

## Example

```c
on ethernetStatus *
{
  switch(this.status)
  {
    case 0:
      write("Ethernet link on Eth%d is down", this.msgChannel );
      break;
    case 1:
      write("Ethernet link on Eth%d is up with %dbit/sec", this.msgChannel , this.bitrate );
  }
}
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| status 0: Link down 1: Link up | long | Read only |
| bitrate Bit rate in kBit/sec | dword | Read only |
| msgChannel Application channel, i.e. Eth 1 | word |  |
| hwChannel Hardware channel. If not supported by network interface, value is 1. | word | Only with Vector Interfaces, i.e. VN5640, with operation mode with more than 1 hardware channel. |
| time_ns Timestamp of the status change | int64 | read only |
