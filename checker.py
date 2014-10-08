import subprocess
import string
import os

answers = ['hello world', 'hello world', '1 1 2 3 5 8 13 21 34 55 89 144', 'abcdefghijklmnopqrstuvwxyz', 'bubbles','True', 'True']

bestSolutionChars = [1000, 1000, 1000, 1000, 1000, 1000, 1000]
bestSolutionUser = ['', '', '', '', '', '', '']

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
    maxProblem = 7;

    while(currentProblem <= maxProblem):
        currentfile = user + '/' + str(currentProblem + 1) + '.py'

        try:
            commandline = "python "+currentfile

            if currentProblem == 4:
                commandline = commandline + " 1 2 9 1 0 -5 bubbles trojanman code golf bubbles bubbles"
                output = subprocess.check_output(commandline, shell=True).rstrip()
            elif currentProblem == 5:
                commandline = commandline + " racecar racecar"
                output = subprocess.check_output(commandline, shell=True).rstrip()
            elif currentProblem == 6:
                commandline = commandline + " penis snipe"
                output = subprocess.check_output(commandline, shell=True).rstrip()
            else:
                output = subprocess.check_output(commandline, shell=True).rstrip()

            print 'output is: ' + output
            print 'answer is: ' + answers[currentProblem]
            if(output == answers[currentProblem]):
                char = 0;
                # Count number of characters
                f = open(currentfile, "r")
                for line in f:
                    char += len(line)

                    # Don't allow o's or i's
                    if(currentProblem == 0):
                        for x in line:
                            if x == 'o' or x == 'i':
                                print 'used an o or i'
                                char += 1000

                    # Don't allow o's or i's
                    if(currentProblem == 1):
                        for x in line:
                            if x == '\"' or x == '\'':
                                print 'used an \' or \"'
                                char += 1000
                print char

                if(char > 0 & char < bestSolutionChars[currentProblem]):
                    print 'best solution ' + str(bestSolutionChars[currentProblem])
                    bestSolutionChars[currentProblem] = char
                    bestSolutionUser[currentProblem] = user
        except:
            currentProblem += 1
            continue
        currentProblem += 1

for i in range (0, len(bestSolutionChars)):
    print 'Problem #' + str(i + 1) + '\t ' + str(bestSolutionChars[i]) + ' characters, ' + bestSolutionUser[i]
