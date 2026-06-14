# Iso11783IL_OPDeactivate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPDeactivate( ); // form 1
```

## Description

The function terminates the connection to the Virtual Terminal.

The Delete Object Pool command is executed to log off from the Virtual Terminal. The Maintenance message is not longer sent. The Object Pool API changes to state Not Active.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPDeactivate( );
```

## Availability

| Since Version |
|---|
