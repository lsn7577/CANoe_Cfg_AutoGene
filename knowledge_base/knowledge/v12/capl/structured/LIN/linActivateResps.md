# linActivateResps

> Category: `LIN` | Type: `function`

## Syntax

```c
long linActivateResps(); // form 1
```

## Description

Reactivates all frame responses published by the calling Slave node according to the LIN database file (LDF), after having been previously deactivated by linDeactiveResps() or linResetSlave().

Per default all frame responses are activated for Slave nodes on measurement start i.e. it is assumed that Slave nodes have non-volatile memory.

LIN2.0 Slave nodes will automatically activate responses for re-configurable frames on receiving valid reconfiguration commands i.e. AssignFrameID.

Individual frame responses can be activated manually using the function linSetRespCounter.

With form 2 you can activate the Slave responses of the selected Slave node (nodeName). If the parameter nodeName is not set or an empty string is given, the Slave responses of the node invoking this function will be deactivated.

Form 2 has only an effect if the target is a program node that was assigned to a Slave node from the selected LIN database.

## Return Values

Number of activated frame responses or -1 if an error occurs.

## Availability

| Since Version |
|---|
