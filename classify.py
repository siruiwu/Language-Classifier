import sys
import pickle

from d_model import DecisionModel
from ada_model import AdaModel


def train(examples, out_file, learner):
    """
    Train a learner on some examples and saves
    the resulting model to a file.

    :param examples: training data
    :param out_file: output file
    :param learner: "ada" or "dt"

    :return:
    """
    if learner == "dt":
        model = DecisionModel(train_file=examples, out_file=out_file)
    else:
        model = AdaModel(train_file=examples, out_file=out_file)

    model.train()


def predict(h_file, test_file):
    """
    Loads a hypothesis (model) from h_file and
    uses it to predict the results of instances
    in a test file.

    :param h_file: model file
    :param test_file: test file
    """
    h_file = open(h_file, "rb")
    model = pickle.load(h_file)

    h_file.close()
    model.test(test_file)


def usage(train_msg=True, predict_msg=True):
    if train_msg:
        print("Usage: python3 classify.py train <examples> <hypothesisOut> <learning-type>")

    if predict_msg:
        print("Usage: python3 classify.py predict <hypothesis> <file>")

    exit(1)


def main():
    """
    Main function. Accepts user input.
    """
    if len(sys.argv) < 2:
        usage()

    action = sys.argv[1]

    if action == "train":
        if len(sys.argv) < 5:
            usage(predict_msg=False)

        examples = sys.argv[2]
        out_file = sys.argv[3]
        learner = sys.argv[4]

        print("Training...")
        train(examples, out_file, learner)
        print("Done.")

    elif action == "predict":
        if len(sys.argv) < 4:
            usage(train_msg=False)

        h_file = sys.argv[2]
        test_file = sys.argv[3]

        predict(h_file, test_file)


if __name__ == '__main__':
    main()
