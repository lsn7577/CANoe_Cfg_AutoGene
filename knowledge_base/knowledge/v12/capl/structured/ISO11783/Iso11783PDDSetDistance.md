# Iso11783PDDSetDistance

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783PDDSetDistance( dword ecuHandle, dword distance );
```

## Description

The distance covered is set with this function. The value is needed for the distance trigger and should be updated cyclically.

## Return Values

Error code

## Example

```c
void ReceiveGBSDFromTractor( 
 pg GroundBasesSpeedPG thisPG ){
 Iso11783PDDSetDistance( ecuHandle, thisPG.GroundBasedDistance.phys );
}
```

## Availability

| Since Version |
|---|
