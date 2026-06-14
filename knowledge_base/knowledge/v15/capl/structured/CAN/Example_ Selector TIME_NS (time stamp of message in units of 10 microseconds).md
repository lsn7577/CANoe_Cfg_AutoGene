# Example: Selector TIME_NS (time stamp of message in units of 10 microseconds)

> Category: `CAN` | Type: `selector`

### Example Selector TIME_NS (time stamp of message in nanoseconds)

Typ int64 (signed 64 bit integer) – only readable.

```c
On message CAN1.100 {
  Write("CAN – Frame with time %I64d received", this.time_ns);
```
