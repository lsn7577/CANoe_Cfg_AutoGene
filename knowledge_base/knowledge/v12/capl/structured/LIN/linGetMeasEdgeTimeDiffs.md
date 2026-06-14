# linGetMeasEdgeTimeDiffs

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linGetMeasEdgeTimeDiffs(dword arrSize, float timeDiffs[]);
```

## Description

This function retrieves the result of a falling edge difference measurement which has been started with linMeasEdgeTimeDiffs. Note that for each byte measured four time differences will be returned, although all of them might be 0 (if there had been only one falling edge in the measured byte). This means that time differences 0 to 3 contain the values for the first measured byte, time differences 4 to 7 contain the values for the second measured byte, etc.

The results are sorted in ascending order by the indices of the measured bytes.

## Return Values

Returns the number of time differences copied into the timeDiffs-array.

## Availability

| Since Version |
|---|
