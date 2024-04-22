# DOSBox Worker

DOSBox Worker is the worker version of [DOSBOX Direct](dosbox-direct.md) backend. It runs in own browser thread, so it's never 
block the browser. **This version is recommended to use in most cases.**

You can create it like this:
```Javascript
const ci = await emulators.dosboxWorker(bundle);
```

Read [Estimating performance](estimating-performance.md) if you want to compare performances of Direct and Worker versions.
