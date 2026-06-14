# coOnBootUp

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coOnBootUp( dword nodeId );
```

## Description

This function is called if a boot-up message was registered on the bus. Each CANopen® node sends this message after the reset during the transition into the state pre-operational.

## Return Values

—

## Example

```c
void coOnBootUp(dword nodeId){
  write( "BootUp of node %d recognized", nodeId );
}
```

## Availability

| Up to Version |
|---|
