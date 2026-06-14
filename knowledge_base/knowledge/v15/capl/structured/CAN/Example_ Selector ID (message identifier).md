# Example: Selector ID (message identifier)

> Category: `CAN` | Type: `selector`

### Example Selector ID (message identifier)

```c
on message * {
  if (this.ID == 0x600) {
    write("message 0x600 received; triggering logging...");
    trigger();
  }
}
```
