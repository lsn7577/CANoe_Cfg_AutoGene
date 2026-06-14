# mostConfigureBusloadAsync

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostConfigureBusloadAsync (long channel, long rate, long countertype, long counterpos, long destadr, long pktdatalen, BYTE pktdata[])
```

## Description

The function configures the bus load generator for the asynchronous channel. With the specified rate the generator tries to send packets.Due to arbitration delays, the bus load actually generated can deviate from the specified rate.

As an option, the packets can be supplied with a sequence counter.

Load generation can be started with the mostGenerateBusloadAsync() function.

Bus load can also be generated without CAPL programming using the MOST Stress Window.

## Return Values

<= 0: See error codes

## Availability

| Since Version |
|---|
