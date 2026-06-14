# SecurityLocalStopControlSimulationNode

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalStopControlSimulationNode(char nodeName[], char networkName[])
```

## Description

Stops controlling (deregistration) the specified simulation node on the specified network.

After a successful deregistration, you cannot call any SecurityOfNode…() Functions at the previously registered node, neither you will receive any OnSecurityOfNode… callbacks .

You have to call SecurityLocalStartControlSimulationNode to register.

## Return Values

1: SuccessA Value of 1 means that the action was successful. A value less than or equal to 0 means error. A value larger than 1 means warning.

## Availability

| Since Version |
|---|
