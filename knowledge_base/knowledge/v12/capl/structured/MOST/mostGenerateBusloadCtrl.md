# mostGenerateBusloadCtrl

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGenerateBusloadCtrl (long channel, long msgs)
```

## Description

The function sends cyclical messages to the control channel. Use the mostConfigureBusloadCtrl() function to specify the send parameters and contents of the message.

This function shows no effect if the StressNIC is not set to slave mode. For that purpose use mostSetStressNodeParameter function with the proper parameter.

## Return Values

<= 0: See error codes

## Availability

| Since Version |
|---|
