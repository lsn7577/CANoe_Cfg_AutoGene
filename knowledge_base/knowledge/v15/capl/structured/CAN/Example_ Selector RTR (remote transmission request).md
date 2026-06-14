# Example: Selector RTR (remote transmission request)

> Category: `CAN` | Type: `selector`

### Example Selector RTR (remote transmission request)

```c
// send remote frame
message 0x100 rmsg;
rmsg.RTR = 1;
output(rmsg);
```
