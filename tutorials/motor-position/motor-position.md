
<table>
<td><img src="https://user-images.githubusercontent.com/44644848/171729465-95d15fc9-1337-4082-8cf9-6ce7e46fd641.jpg"  width=500/></td>
<td><p><h1>DC Motor Position Controller Design</h1></p>
<p>Tuning a PID controller for a DC Motor Position System.</p>
</table>

## Objective
In this example using the Ziegler-Nichols method for empirically tuning the PID controller, we will show how to design and simulate a PID controller for controlling the position of a DC motor shaftin Collimator

## Project Description

```html
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.1/styles/agate.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.1/highlight.min.js"></script>
<!-- and it's easy to individually load additional languages -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.1/languages/go.min.js"></script>

<script src="https://unpkg.com/highlightjs-copy/dist/highlightjs-copy.min.js"></script>
<link rel="stylesheet" href="https://unpkg.com/highlightjs-copy/dist/highlightjs-copy.min.css"/>
<script>
 hljs.highlightAll();
 hljs.addPlugin(new CopyButtonPlugin());
</script>
```

### Motor Position Model

The motor is conceptually modeled as in Figure 1 with the parameters given in Table 1.
<br /><br />
<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/171734152-10bee237-df67-4050-b2b7-5feb31295afc.png"  width="400"/>
</p>

## Results

