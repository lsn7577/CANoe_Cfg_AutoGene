# elCount

> Category: `Other` | Type: `function`

## Syntax

```c
long elcount(...) // if used with arrays which are function parameters
```

## Description

Determines the number of elements of an array.

## Return Values

Number of elements.

## Example

```c
void bsp(int ar[]) {
int i;
for(i=0; i < elCount(ar); i++)
...
}

void bsp2(byte ar[][]) {
int i, j;
for(j=0; j < elCount(ar); j++ )
for(i=0; i<= elCount(ar[j]); i++ )
...
}
```

## Availability

| Since Version |
|---|
