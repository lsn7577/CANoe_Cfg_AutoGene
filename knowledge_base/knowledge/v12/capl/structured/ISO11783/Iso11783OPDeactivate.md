# Iso11783OPDeactivate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPDeactivate( dword ecuHandle );
```

## Description

The function terminates the connection to the Virtual Terminal.

The Delete Object Pool command is executed to log off from the Virtual Terminal. The Maintenance message is not longer sent. The Object Pool API changes to state Not Active.

## Return Values

0 or error code

## Example

```c
Iso11783OPDeactivate( 
 handle );
```

## Availability

| Since Version |
|---|
