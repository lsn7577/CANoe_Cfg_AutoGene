# mostConfigureBusloadEthPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostConfigureBusloadEthPkt(long channel, long rate, long countertype, long counterpos, int64 srcadr, int64 destadr, long datalen, BYTE data[])
```

## Description

The function configures the bus load generator for the Ethernet channel.

As an option, the packets can be supplied with a sequence counter.

Load generation can be started with the mostGenerateBusloadEthPkt function.

Bus load can also be generated without CAPL programming using the MOST Stress Window.

## Return Values

See error codes

## Availability

| Since Version |
|---|
