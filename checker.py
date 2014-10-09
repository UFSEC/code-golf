from __future__ import print_function
import argparse
import collections
import os
import StringIO
import subprocess
import tempfile

def code_equals_output(code, output):
    return code == output

def code_not_contains(*strings):
    """Return a validator that ensures the code doesn't contain the given strings"""
    def validate(code, output):
        return all(s not in code for s in strings)
    return validate

def c(*test_cases, **kwargs):
    """Helper for constructing challenge tuples"""
    if len(kwargs) > 0 and 'validator' not in kwargs:
        # In Python 3 we can list specific keyword arguments after a starred
        # argument, but in Python 2 we have to use ** and check manually.
        raise TypeError("'validator' is the only valid keyword argument")
    return (test_cases, kwargs.get('validator'))

challenges = {
    # challenge_basename: ([(args, output), ...], validation_func)
    "1": c(([], "hello world"), validator=code_not_contains("i", "o")),
    "2": c(([], "hello world"), validator=code_not_contains("'", '"')),
    "3": c(([], "1 1 2 3 5 8 13 21 34 55 89 144")),
    "4": c(([], "a b c d e f g h i j k l m n o p q r s t u v w x y z")),
    "5": c(("1 2 9 1 0 -5 bubbles trojanman code golf bubbles bubbles".split(), "bubbles"),
           (["blarg"], "blarg"),
           ("1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6".split(), "5")),
    "6": c((["racecar"], "True"),
           (["alphabet"], "False"),
           (["supercalifragilisticexpialidociousuoicodilaipxecitsiligarfilacrepus"], "True")),
    "7": c(("penis snipe".split(), "True"),
           ("badge debag".split(), "True"),
           ("apple peal".split(), "False"),
           ("torchwood doctorwho".split(), "True"),
           ("loop poll".split(), "False")),
    "8": c(validator=code_equals_output),
}

parser = argparse.ArgumentParser()
parser.add_argument("user", metavar="USER", nargs="?", default=None,
                    help="User to score in detail (instead of scoring everyone)")
cli_args = parser.parse_args()
details = bool(cli_args.user)

tmpdir = tempfile.mkdtemp()

scores = {}
for user in os.listdir("."):
    if not os.path.isdir(user) or user == ".git":
        continue
    if details and user != cli_args.user:
        continue

    print(">> Scoring %s" % user)
    scores[user] = {}
    for challenge_name, (test_cases, validator) in sorted(challenges.items()):
        state = "passed"
        script = os.path.abspath(os.path.join(user, "%s.py" % challenge_name))
        try:
            script_source = open(script).read()
        except IOError:
            state = "missing"
            continue
        script_length = len(script_source)

        # Check the test cases
        print("Challenge %s:" % challenge_name, end=" ")
        for extra_args, answer in test_cases:
            args = ["python2", script]
            if extra_args:
                args.extend(extra_args)

            p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 cwd=tmpdir)
            output, stderr = p.communicate()

            if p.returncode != 0:
                state = "crashed"
                break

            if output.rstrip() != answer:
                state = "failed"
                break

            if validator and not validator(script_source, output):
                state = "cheated"
                break

        print("%s! (%s characters)" % (state, script_length))
        if state == "passed":
            scores[user][challenge_name] = script_length
        elif details and state == "failed":
            print("Expected: %s" % answer)
            print("Got     : %s" % output.rstrip())
        elif details and state == "crashed":
            print(stderr)

# Compile scores into a nice structure
def highscore(score=float('inf'), users=None):
    return (score, users or [])
best_scores = collections.defaultdict(highscore)

for user, user_scores in scores.items():
    for challenge_name, score in user_scores.items():
        current_score, current_users = best_scores[challenge_name]
        if score < current_score:
            best_scores[challenge_name] = highscore(score, [user])
        elif score == best_scores[challenge_name][0]:
            best_scores[challenge_name] = highscore(score, current_users + [user])

if not details:
    print(">> Best scores")
    for challenge_name, (score, users) in sorted(best_scores.items()):
        print("Challenge %s: %s characters: %s" % (challenge_name, score, ", ".join(users)))
