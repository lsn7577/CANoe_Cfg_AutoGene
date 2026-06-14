# Iso11783IL_PDDOnPDM

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDOnPDM( long command, long parameter, long senderAddress, long pddStatus );
```

## Description

The callback method is called from the ISO11783 Interaction Layer if the ISO11783 Interaction Layer receives the Process Data Message parameter group (PDM pg).

## Example

The following example is to be used in the environment, where more than one Task Controller is available and determines, that the current node has to communicate with the Task Controller with the address: 246:

```c
LONG Iso11783IL_PDDOnPDM (long command, long parameter, long senderAddress, long pddStatus)
{
  if (command != 0x0e)
    return 1; //isn't a TC status
  if (pddStatus != 3)
    return 1; //node isn't in a state 'WaitForStatus'
  if (senderAddress == 247)
    return 1;
  else
    return 0;
}
```

## Availability

| Since Version |
|---|
