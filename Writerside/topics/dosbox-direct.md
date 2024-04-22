# DOSBox Direct

DOS Direct is an emulation backend based on DOSBox, you can create it with following command:

```Javascript
const ci = await emulators.dosboxDirect(bundle);
```

Direct version is universal, it can work in Node.js environment. But it has a strong disadvantage: it's working on the 
main browser thread. So it can easily hang a browser for some amount of time, and not be very responsive.

> [DOSBox Worker](dosbox-worker.md) is a more preferred version of the emulator backend, because it does not block the browser.
> 
{style="tip"}

### Accessing file system

In direct mode you can easily access emscripten module:

```Javascript
const ci = await emulators.dosboxDirect(bundle);
ci.transport.module // <-- emscripten module
```

Emscripten module provide lowlevel api to change [file system](https://emscripten.org/docs/api_reference/Filesystem-API.html):

```Javascript
const ci = await emulators.dosboxDirect(bundle);
ci.transport.module.FS // <-- emscripten FS api
```

You can also rescan DOS devices:
```Javascript
const ci = await emulators.dosboxDirect(bundle);
ci.transport.module._rescanFilesystem();
```

### Accessing memory

In direct mode you can dump whole memory of dos:

```Javascript
const ci = await emulators.dosboxDirect(bundle);
ci.transport.module._dumpMemory(copyDosMemory);
ci.transport.module.memoryContents // <-- now you can access contents using this var
```

If you need to copy entire memory pass `true` as argument.
The `memoryContents` contains following:


```Javascript
{
        "memBase": ...,
        "ip": ...,
        "flags": ...,
        "registers": {
            "ax": ...,
            "cx": ...,
            "dx": ...,
            "sp": ...,
            "bp": ...,
            "si": ...,
            "di": ...
        },
        "segments_values": {
            "es": ...,
            "cs": ...,
            "ss": ...,
            "ds": ...,
            "fs": ...,
            "gs": ...
        },
        "segments_physical": {
            "es": ...,
            "cs": ...,
            "ss": ...,
            "ds": ...,
            "fs": ...,
            "gs": ...
        },
        "numPages": ...,
        "memoryCopy": ...
}
```

### Pausing execution

In direct mode, you can pause the Dosbox execution loop without pausing the
emscripten loop.  This lets you pause and inspect the current memory, for
instance.

```Javascript
const ci = await emulators.dosboxDirect(bundle);
ci.transport.module._pauseExecution(true);
```

The `_pauseExecution` function takes as its argument whether it should be
paused or should resume.  To resume once you have completed:

```Javascript
ci.transport.module._pauseExecution(false);
```
