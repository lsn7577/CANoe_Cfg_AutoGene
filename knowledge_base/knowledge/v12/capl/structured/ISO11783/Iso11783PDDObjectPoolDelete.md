# Iso11783PDDObjectPoolDelete

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDObjectPoolDelete( dword ecuHandle );
```

## Description

The function deletes the current device description object pool and sends an Object-pool Delete message to the Task Controller.

Contrary to Iso11783PDDDelete the connection to the Task Controller is not removed.

## Return Values

Error code

## Example

```c
if (Iso11783PDDObjectPoolDelete( ecuHandle ) == 0) {
  write("Object pool is deleted and Object-Pool delete message is sent successfully");
}
```

## Availability

| Since Version |
|---|
