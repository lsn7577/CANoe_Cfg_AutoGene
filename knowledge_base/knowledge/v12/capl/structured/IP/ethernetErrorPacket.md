# ethernetErrorPacket

> Category: `IP` | Type: `function`

## Syntax

```c
ethernetErrorPacket <errorPacket var>;
```

## Description

Can be use in on ethernetErrorPacket handler to access packet data.

## Example

```c
on ethernetErrorPacket *
{
  write("Received Ethernet error packet on Eth%d", this.msgChannel );
  output( this ); // only required in CAPL node in measurement setup!
}
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| time_ns Point in time, units: nanoseconds | int64 | Read only |
| dir | byte | Read only |
| msgChannel Application channel, i.e. Eth 1. | word | — |
| hwChannel Hardware channel. If not supported by network interface, value is 1. | word | Only with Vector Interfaces, i.e. VN5640, with operation mode with more than 1 hardware channel. |
