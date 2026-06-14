# OnMostApInstID

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostApInstID()
```

## Description

If the InstID of the associated function block changes, the CAPL node is informed by the event procedure OnMostApInstID (only with an active MOST Application Socket). If the functional address {FBlockID, InstID} occurs more than once in the network a change to the InstID is initiated by the NetworkMaster (Message: NetBlock.FBlockIDs.SetGet(FBlockID, OldInstID, NewInstID)).

The new valid InstID may be polled by mostApGetInstID.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

CAPL nodes are transparent to the controller events. Please use the Multibus Filter or MOST Filter, to filter these events in nodal sequences.

In the Simulation Setup event procedures are only called if the event occurs on the channel allocated to the CAPL node.

## Return Values

—

## Availability

| Since Version |
|---|
