# A664InitPayload

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664InitPayload (a664Message aMessage)
```

## Description

The payload section (excluding sequence number) of an AFDX message is set using the current Tx-values of the internal signal list. These are typically set by CAPL signal value assignments, panels, signal generators, start value etc.

The message must be defined in the database and must contain signals (no protocol oriented types).

## Return Values

<success>

## Example

```c
a664Message TESTMSG_ALLTYPES testMsg = { msgChannel = 1};
a664InitPayload (testMsg); 	// set payload to last known signal values
a664TriggerMessage(testMsg, 1);
```

## Availability

| Since Version |
|---|
