# Iso11783OPChangeSoftKeyMask

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeSoftKeyMask( dword ecuHandle, dword maskID, dword softKeyMaskID );
```

## Description

The function changes the soft key mask of a data mask. A Change Soft Key Mask command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeSoftKeyMask( handle, 1000, 1050 );
```

## Availability

| Since Version |
|---|
