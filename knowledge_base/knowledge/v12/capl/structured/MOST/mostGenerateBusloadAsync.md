# mostGenerateBusloadAsync

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGenerateBusloadAsync (long channel, long pkts)
```

## Description

The function sends cyclical packets to the asynchronous channel. Use the mostConfigureBusloadAsync() or mostSetStressNodeParameter() function to specify the send parameters and contents of the packets.

This function shows no effect if the StressNIC is not set to slave mode. For that purpose use mostSetStressNodeParameter with the proper parameter.

## Return Values

<= 0: See error codes

## Availability

| Since Version |
|---|
