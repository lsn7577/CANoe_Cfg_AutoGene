# cancelTimer

> Category: `Other` | Type: `function`

## Syntax

```c
void cancelTimer(msTimer t);
```

## Description

Stops an active timer.

## Return Values

—

## Example

```c
variables {
msTimer takt;
message 100 data = {dlc = 1, byte(0) = 0xFF, dir = Tx};
}
on Timer takt{
output(data);
setTimer(takt, 200);
}
on key F1 {
cancelTimer(takt); // cancel timer
write("canceled");
}
on key F2 {
setTimer(takt, 200); // set timer to 200ms
write("start");
}
```

## Availability

| Since Version |
|---|
