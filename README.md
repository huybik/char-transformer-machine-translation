# char-transformer-machine-translation
**Translate text with Transformer sequence to sequence architecture using only characters, implement in Pytorch**

<p align = "center"> 
<img src='https://www.quotemaster.org/images/04/046e60f1f0f4f86cb84ac4eae813f55c.jpeg' width=400>
</p>
<p align = "center"> Light weight text translation </p>

Most implementations on the net of transformer text translation use word or byte-pair with 10000+ vocabularies as input which takes ages to train. This implementation use only characters in text data as vocabulary (<300 chars), so I can train everything from scratch in under 30 minutes. I also include a compact beam search implementation at the end.

This implementation inspired by <a href='https://github.com/karpathy/minGPT'>Andrej Karpathy MinGPT</a>


