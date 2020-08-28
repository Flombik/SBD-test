from transformers import AutoTokenizer
import argparse


def tokenize(text):
    global tokenizer
    tokens = tokenizer.tokenize(text)
    print(tokens)


def args_parser_init():
    parser = argparse.ArgumentParser(
        description='Tokenize text with "transformers"')
    parser.add_argument('texts', metavar='TEXTS', type=str,
                        nargs='+', help="Texts to tokenize")
    parser.add_argument('--model', default='bert-base-german-cased',
                        type=str, help='The language model used by the tokenizer')
    return parser


if __name__ == "__main__":
    parser = args_parser_init()

    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    # tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-german-europeana-cased")

    for text in args.texts:
        tokenize(text)
