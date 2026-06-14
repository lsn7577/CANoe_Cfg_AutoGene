# Iso11783IL_PDDObjectPoolDeactivate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDObjectPoolDeactivate( ); // form 1
```

## Description

The function sends an Object-pool Deactivate message to the Task Controller and disconnects the connection to the Task Controller.

## Return Values

error code

## Example

```c
if (Iso11783IL_PDDObjectPoolDeactivate ( ) == 0) {
  write( "Node has disconnected from the Task Controller" );
}
```

## Availability

| Since Version |
|---|
