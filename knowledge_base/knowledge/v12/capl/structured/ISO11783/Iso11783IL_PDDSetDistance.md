# Iso11783IL_PDDSetDistance

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDSetDistance( dword distance ); // form 1
```

## Description

The distance covered is set with this function. The value is needed for the distance trigger and should be updated cyclically.

## Example

```c
void ReceiveGBSDFromTractor( 
 pg GroundBasesSpeedPG thisPG ){
 Iso11783IL_PDDSetDistance( thisPG.GroundBasedDistance.phys );
}
```

## Availability

| Since Version |
|---|
