# Iso11783IL_OPChangeSoftKeyMask

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeSoftKeyMask( dword maskID, dword softKeyMaskID ); // form 1
```

## Description

The function changes the soft key mask of a data mask. A Change Soft Key Mask command is sent to the Virtual Terminal.

If parameter maskType is not used the mask type is determined by the mask object.

## Example

```c
Iso11783IL_OPChangeSoftKeyMask( 1000, 1050 );
```

## Availability

| Since Version |
|---|
