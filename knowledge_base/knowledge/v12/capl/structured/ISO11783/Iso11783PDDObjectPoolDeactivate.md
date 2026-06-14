# Iso11783PDDObjectPoolDeactivate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDObjectPoolDeactivate( dword ecuHandle );
```

## Description

The function sends an Object-pool Deactivate message to the Task Controller and disconnects the connection to the Task Controller.

## Return Values

Error code

## Example

```c
if (Iso11783PDDObjectPoolDeactivate ( ecuHandle ) == 0) {
  write( "Node has disconnected from the Task Controller" );
}
```

## Availability

| Since Version |
|---|
