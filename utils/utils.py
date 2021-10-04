import random
import numpy as np
import torch
import torch.nn as nn
from torch.nn import functional as F

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def pickle(file_path, data=None):
    import bz2
    import pickle
    
    if data is not None:
        with bz2.BZ2File(file_path, 'wb') as f:
            pickle.dump(data, f)
            data = True
    else:
        with bz2.BZ2File(file_path, 'rb') as f:
            data = pickle.load(f)

    return data

def bleu_score(references, candidates):
    from nltk.translate.bleu_score import corpus_bleu

    # reference and candidate is list of strings
    references = [[sen.split(' ')] for sen in references]
    candidates = [sen.split(' ') for sen in candidates]
    score = corpus_bleu(references, candidates)*100
    return score, references, candidates

