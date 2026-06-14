# Iso11783IL_TIMConnectToServer

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMConnectToServer(dbNode server); // form 1
```

## Description

Starts a TIM connection to a TIM server.

Starts initialization with a server by switching to state Automaton unavailable and waits for the status message of the server.

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
