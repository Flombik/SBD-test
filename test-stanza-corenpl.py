import stanza
from stanza.server import CoreNLPClient
import argparse


def tokenize(text):
    with CoreNLPClient(annotators=['tokenize', 'ssplit'], timeout=30000, memory='4G', be_quiet=True, properties='german') as client:
        ann = client.annotate(text)

        sents = []

        for sent in ann.sentence:
            temp = ''
            for t in sent.token:
                temp += t.word + ' '
            sents.append(temp)

        print(sents)


def args_parser_init():
    parser = argparse.ArgumentParser(
        description='Tokenize text with "CoreNLP"')
    parser.add_argument('texts', metavar='TEXTS', type=str,
                        nargs='+', help="Texts to tokenize")
    return parser


if __name__ == "__main__":
    parser = args_parser_init()

    args = parser.parse_args()

    stanza.install_corenlp()
    stanza.download_corenlp_models(model='german', version='4.1.0')

    for text in args.texts:
        tokenize(text)
