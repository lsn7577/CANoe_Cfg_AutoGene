# Iso11783OPChangeListItem

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeListItem( dword ecuHandle, dword inputID, dword index, dword itemID );
```

## Description

The function changes an item in an input list object. A Change List Item command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeListItem( handle, 1200, 1, 1250 );
```

## Availability

| Since Version |
|---|
