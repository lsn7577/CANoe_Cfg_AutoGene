# getCardType

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long getCardType();
```

## Description

Determines the type of CAN platform being used. Is needed e.g. to program the BTR / OCR values.

## Return Values

17: for Vector drivers

## Example

```c
...
switch(getCardType()) {
case 6: setOcr(0,0x02);
   break;
case ...
default:
   write("Unknown driver %d", getCardType());
   break;
}
...
```

## Availability

| Up to Version |
|---|
