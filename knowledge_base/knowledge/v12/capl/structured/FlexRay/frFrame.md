# frFrame

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frFrame <frame name> <frame var>;
```

## Description

Can be used to create a FlexRay send object. The object data can be manipulated by selectors associated with this object. Other object characteristics can be read out from selectors.

Objects are then registered using the frSetSendFrame and are sent using the frUpdateStatFrame or frOutputDynFrame functions.

## Example

This is an example for using the Frame object in arrays.

All objects of an array must be initialized with an appropriate frame definition!

```c
variables
{
  frFrame (1,0,1) frm1;

  // All objects are equal:
   frFrame (2,0,1) frArray1[10];

  // All objects may be different:
  frFrame * frArray2[3] = { (3,0,1), <FrameNameFromDB>, frm1 };
}
```

## Availability

| Since Version |
|---|
