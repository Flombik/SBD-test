import stanza
import argparse

def tokenize(text):
    global nlp    
    doc = nlp(text)

    print([sentence.text for sentence in doc.sentences])


def args_parser_init():
    parser = argparse.ArgumentParser(
        description='Tokenize text with "stanza"')
    parser.add_argument('texts', metavar='TEXTS', type=str,
                        nargs='+', help="Texts to tokenize")
    return parser


if __name__ == "__main__":
    parser = args_parser_init()

    args = parser.parse_args()

    stanza.download('de')
    nlp = stanza.Pipeline('de', processors='tokenize')

    for text in args.texts:
        tokenize(text)
