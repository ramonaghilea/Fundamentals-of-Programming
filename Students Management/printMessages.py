def printReposWithMessage(msg, studRepo, disRepo, gradeRepo):
    print("-"*15 + msg + "-"*15)
    if studRepo != None:
        print("Students:\n" + str(studRepo))
    if disRepo != None:
        print("Disciplines:\n" + str(disRepo))
    if gradeRepo != None:
        print("Grades:\n" + str(gradeRepo))