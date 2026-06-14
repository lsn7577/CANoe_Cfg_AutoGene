# SCC_SendPreparedMessage

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SendPreparedMessage ( ) // form 1
```

## Description

Sends a message created using one of the Create-functions. Use the function call with parameter ConfigSection to create a signed message using the certificate name from the XML config. Else an unsigned message is sent.

## Return Values

1 if successful

## Availability

| Since Version |
|---|
