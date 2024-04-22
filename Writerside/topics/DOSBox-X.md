# DOSBox-X

The DOSBox-X emulation backend is capable of running operating systems up to Windows 98/ME. You can utilize it to run
Windows games or arbitrary Windows programs. It may be a bit slower than traditional DOSBox emulation.

DOSBox-X emulation supports execution in worker, networking, and all other features that js-dos provides.

Typically, Windows distributions are known for their larger file sizes. To address this, we recommend using virtual makevm drives. 
Additionally, we offer prebuilt images of fully configured Windows 95/98, streamlining the installation process for your chosen game.

Worker instance:
```Javascript
const ci = await emulators.dosboxXWorker(bundle);
```

Direct instance:
```Javascript
const ci = await emulators.dosboxXDirect(bundle);
```
