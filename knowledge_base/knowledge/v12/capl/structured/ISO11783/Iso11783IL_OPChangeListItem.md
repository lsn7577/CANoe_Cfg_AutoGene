# Iso11783IL_OPChangeListItem

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeListItem( dword inputID, dword index, dword itemID ); // form 1
```

## Description

The function changes an item in an input list object. A Change List Item command is sent to the Virtual Terminal.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPChangeListItem( 1200, 1, 1250 );
```

## Availability

| Since Version |
|---|
