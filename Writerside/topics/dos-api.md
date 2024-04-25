# Getting Started

js-dos does not require any backend to start. You need to have some static website hosting where you put
your webpage with DOS.

You can start with any template of webpage you want. You only need some div element where to put 
dos window.

## Adding js-dos to your web page

This is common thing in web development, you need to add js-dos related scripts to your webpage.
js-dos provide a CDN with latest version, just add this html to `<head>` section of page:

```html
<!-- js-dos style sheet -->
<link rel="stylesheet" href="https://v8.js-dos.com/latest/js-dos.css">

<!-- js-dos -->
<script src="https://v8.js-dos.com/latest/js-dos.js"></script>
```

## Provide js-dos bundle to run

The easiest way to run some program is to prepare [js-dos bundle](jsdos-bundle.md). You can do it 
manually, but easier way is to use [Studio](doszone.md).

In this example we will use a bundle of Digger game.
Direct link to it: 
```
https://cdn.dos.zone/original/2X/9/9ed7eb9c2c441f56656692ed4dc7ab28f58503ce.jsdos
```

## Write script to run DOS

Last part: we need to provide create some div element and tell js-dos to run bundle using that div:

```html
<div id="dos"></div>

<script>
    Dos(document.getElementById("dos"), {
        url: "https://cdn.dos.zone/original/2X/9/9ed7eb9c2c441f56656692ed4dc7ab28f58503ce.jsdos",
    });
</script>
```

That is, Dos constructor takes two arguments:

1. div element where to put dos window
2. options with initial configuration


```Typescript
```
{src="examples/digger-v8.html" collapsible="true" collapsed-title="Full page source"}

## Test in browser

Open your test webpage in browser, you should see something like this:

![digger-v8.png](digger-v8.png)

> Do not try to run it using file:// protocol, it will not work.
> You need to host it locally. (http://localhost:8080)
> 
{style="warning"}