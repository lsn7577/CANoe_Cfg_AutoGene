# AfdxOutputPacket

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxOutputPacket( long packet ); // form 1
```

## Description

The specified AFDX message is transmitted with this function call.

Note that the user has complete control of all the transmission scenarios. If the message is defined in an AFDX database the corresponding message attributes (e.g. timing, redundancy) are used for the transmission. CANoe internally uses an AFDX software stack for the message handling.

In the following cases the message needs to be defined in a DBC file and the file needs to be assigned to the actual configuration:

## Availability

| Since Version |
|---|
