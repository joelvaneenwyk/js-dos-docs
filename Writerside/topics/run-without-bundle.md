# Run without bundle

As explained in other topics, the bundle is a preferred way to run DOS program. Bundle can contain much more configuration
that DOSBox excepts, for example, mobile controls, resources, etc.

> If you are looking at the recommended and correct way to run DOS program just create [bundle](jsdos-bundle.md) for it.
> 
{style="warning"}

## Provide dosbox.conf directly

js-dos can work without a bundle, but at least it needs a DOSBox config file to start.
You can create js-dos player by providing config using javascript:

```Javascript
Dos(document.getElementById("app"), {
  dosboxConf: `
[dos]
ver=7.1
hard drive data rate limit=0
floppy drive data rate limit=0

[cpu]
cputype=pentium_mmx
core=auto 
integration device=true

[sblaster]
sbtype=sb16vibra`,
  onEvent: (event, ci) => {
    if (event === "ci-ready") {
        // ci: [[[CommandIterface|command-interface.md]]] is ready
    }
  },
});
```

When you get [command interface](command-interface.md) (ci in example), then you can use [FS API](working-with-fs.md) to work with DOS filesystem.
For example, you can upload program to run in DOSBox. 

Do not forget to mount drive **C:** after that.

