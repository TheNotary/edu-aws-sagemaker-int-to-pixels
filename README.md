# Int to Pixels

A NN example demonstraghting how to train a model to go from an integery, leverage an internal layer, and then output to a 3 x 5 grid. All of the neurons are visually represented and explained in the demo.

###### Parallel Memorization
I want to start with this, because it's more "interpretable" but also, not at all how LLMs memorize information like working URLs.  

###### Serial memorization
I want to pivot to this, where the LLM has only one output neuron and it must output the pixels (in order) before reaching a stop token.  I'm curious if the math works out that this is much more efficient, and what kinds of neural archetecture work best.  

###### Cloud Training

I'd like to deploy this for triaining via a cloud GPU offering using automation, but I looked at the offerings and might put that off for later or actually adopt a manual process through a provider that doesn't have an API.  

## Dev Setup

```
python -m venv .venv
source .venv/bin/activate
```



## Refs

- [Tensorflow basics](https://www.tensorflow.org/tutorials/quickstart/beginner)
- [Memorization in NNs](https://www.youtube.com/watch?v=piF6D6CQxUw)
