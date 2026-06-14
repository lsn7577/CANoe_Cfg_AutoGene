# Iso11783IL_PDDObjectPoolDelete

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDObjectPoolDelete( ); // form 1
```

## Description

The function deletes the current device description object pool and sends an Object-pool Delete message to the Task Controller

Contrary to Iso11783IL_PDDDelete the connection to the Task Controller is not removed.

## Return Values

error code

## Example

```c
if (Iso11783IL_PDDObjectPoolDelete( ) == 0) {
  write("Object pool is deleted and Object-Pool delete message is sent successfully");
}
```

## Availability

| Since Version |
|---|
