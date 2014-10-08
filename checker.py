import subprocess
import string
import os

answers = ['test1', 'test2', 'test', 'test', 'test', 'test']

bestSolutionChars = [1000, 1000, 1000, 1000, 1000, 1000]
bestSolutionUser = ['', '', '', '', '', '']

for x in os.walk('.'):
    user = x[0].split('/')

    # Skip the home directory case
    if(len(user) < 2):
        continue 

    user = user[1]

    # We don't want those git files
    if(user == '.git'):
        continue

    print user

    currentProblem = 0;
    maxProblem = 6;

    while(currentProblem <= maxProblem):
        print 'current problem is ' + str(currentProblem)
        currentfile = user + '/' + str(currentProblem + 1) + '.py'

        try:
            output = subprocess.check_output("python " + currentfile, shell=True).rstrip()
            print 'output is: ' + output
            print 'answer is: ' + answers[currentProblem]
            if(output == answers[currentProblem]):
                char = 0;
                # Count number of characters
                f = open(currentfile, "r")
                for line in f:
                    char += len(line)
                print char

                if(char > 0 & char < bestSolutionChars[currentProblem]):
                    bestSolutionChars[currentProblem] = char
                    bestSolutionUser[currentProblem] = user
        except:
            currentProblem += 1
            continue
        currentProblem += 1

for i in range (0, len(bestSolutionChars)):
    print 'Problem #' + str(i + 1) + '\t ' + str(bestSolutionChars[i]) + ' characters, ' + bestSolutionUser[i]
