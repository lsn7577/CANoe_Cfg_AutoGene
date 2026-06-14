# setMsgTime

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void setMsgTime(message m, NOW);
```

## Description

Assigns to one message the capture time of another message or the current time. This function is deprecated and only serves to establish compatibility with older versions.

## Return Values

—

## Example

```c
setMsgTime(m100, this); // CANalyzer 1.xx & 2.xx
m100.time = this.time; // CANalyzer 2.xx
setMsgTime (m101, now);
```

## Availability

| Up to Version |
|---|
