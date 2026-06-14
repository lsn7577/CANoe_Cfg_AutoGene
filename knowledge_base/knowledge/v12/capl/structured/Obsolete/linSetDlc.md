# linSetDlc

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long linSetDlc(long frameID, long dlc)
```

## Description

Initializes the Data Length Code (i.e. length in bytes) of a LIN frame. This function must be called in the event procedure on preStart. The DLC of each frame ID can only be initialized once using this function.

To change the DLC of a LIN frame during the measurement, use the function linChangeDlc().

Per default the DLC of LIN frames is initialized according to the LIN Description File (LDF). This function is therefore only needed if you are simulating LIN nodes without using an LDF.

## Return Values

If successful a value unequal to zero. Zero will be returned if for example the DLC has already been set for the selected ID.

## Example

Set DLC of a LIN frame not defined in the database.

```c
on preStart
{
...
linSetDLC(0x22, 5);  // set DLC of frame with identifier 0x22 to be 5
...
}
```

## Availability

| Up to Version |
|---|
