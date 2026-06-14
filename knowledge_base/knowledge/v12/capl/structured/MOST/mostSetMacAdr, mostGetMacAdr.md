# mostSetMacAdr, mostGetMacAdr

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetMacAdr(long channel, int64 macAdr)
```

## Description

The functions set and retrieve the 48 bit MAC address of the network interface controller. The MAC address identifies the network node during Ethernet-over-MOST150 communication (see OnMostEthPkt, outputMostEthPkt).

## Return Values

mostSetMacAdr: See error codes

## Example

```c
// Set MAC address on channel MOST 1 to 01:02:03:04:05:06
mostSetMacAdr(1, 0x010203040506LL);
```

## Availability

| Since Version |
|---|
