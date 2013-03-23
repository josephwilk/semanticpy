# SemanticPy

A collection of projects in python looking at semantics. Mostly orientated around search.

## Example

```python
from semanticpy.vector_space import VectorSpace

vector_space = VectorSpace(["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]))

#Search for cat
print vector_space.search(["cat"])

#Show score for relatedness against document 0
print vector_space.related(0) 
```

## Supported

* Vector space search - "http://blog.josephwilk.net/projects/building-a-vector-space-search-engine-in-python.html":http://blog.josephwilk.net/projects/building-a-vector-space-search-engine-in-python.html
* Latent semantic analysis - "http://blog.josephwilk.net/projects/latent-semantic-analysis-in-python.html":http://blog.josephwilk.net/projects/latent-semantic-analysis-in-python.html


## Dependencies

* Porter Stemmer - "http://tartarus.org/~martin/PorterStemmer/python.txt":http://tartarus.org/~martin/PorterStemmer/python.txt
* English stop list - "ftp://ftp.cs.cornell.edu/pub/smart/english.stop":ftp://ftp.cs.cornell.edu/pub/smart/english.stop
* Scipy -  "http://www.scipy.org/":http://www.scipy.org/

#License
(The MIT License)

Copyright (c) 2008-2013 Joseph Wilk

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.