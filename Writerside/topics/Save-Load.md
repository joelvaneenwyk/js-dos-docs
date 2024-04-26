# Persist FS

emulators supports saving and restoring changes made in file system. It works by dumping 
changes of file system into second `bundle` and use it to override original file system
on next load. This feature is backed by [CommandInterface](command-interface.md) `persist` function.

You can implement your own save/load feature like this:

```Typescript
const bunlde = <Uint8Array>;
const ci = await emulators.dosboxWorker(bundle);

// saving
const changesBundle = await ci.persist();

// <new session>

// loading
const ci = await emulators.dosboxWorker([bundle, changesBundle]
```