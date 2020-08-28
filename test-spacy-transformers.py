import spacy
import argparse

def tokenize(text):
    global nlp
    doc = nlp(text)
    print([sent.text for sent in doc.sents])


def args_parser_init():
    parser = argparse.ArgumentParser(
        description='Tokenize text with "spacy"')
    parser.add_argument('texts', metavar='TEXTS', type=str,
                        nargs='+', help="Texts to tokenize")
    parser.add_argument('--model', default='de_trf_bertbasecased_lg',
                        type=str, help='The language model used by the tokenizer')
    return parser


if __name__ == "__main__":
    parser = args_parser_init()

    args = parser.parse_args()

    nlp = spacy.load(args.model)

    for text in args.texts:
        tokenize(text)