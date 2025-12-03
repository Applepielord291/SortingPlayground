# Nigel Garcia
# questions.py
# Question class to display questions cause its funny

class Question:
    question = ""
    codeSnippet = ""
    answers = []
    correctAnswer = 0
    def __init__(self, question, codeSnippet, answers, correctAnswer):
        self.question = question
        self.codeSnippet = codeSnippet
        self.answers = answers
        self.correctAnswer = correctAnswer

mergeSort=[ "1  def merge(firstHalf, secondHalf):",
            "2     finalList = []",
            "3     i, j = 0",
            "4     while i < len(firstHalf) and j < len(secondHalf):",
            "5         if firstHalf[i] <= secondHalf[j]:",
            "6             finalList.append(firstHalf[i])",
            "7             i += 1",
            "8         else:",
            "9             finalList.append(secondHalf[j])",
            "10            j += 1",
            "11    while i < len(firstHalf):",
            "12        finalList.append(firstHalf[i])",
            "13        i += 1",
            "14    while j < len(secondHalf):",
            "15        finalList.append(secondHalf[j])",
            "16        j += 1",
            "17    return finalList",
            "18 def sort(list):",
            "19    length = len(list)",
            "20    if length < 2:",
            "21        return list",
            "22    else:",
            "23        firstHalf = list[:length//2]",
            "24        secondHalf = list[length//2:]",
            "25    return merge(sort(firstHalf), sort(secondHalf))" ]
errorsor3=[ "1  def merge(firstHalf, secondHalf):",
            "2     finalList = firstHalf + secondHalf",
            "3     i, j = 0",
            "4     while i < len(firstHalf) and j < len(secondHalf):",
            "5         if firstHalf[i] <= secondHalf[j]:",
            "6             finalList.append(firstHalf[i])",
            "7             i += 1",
            "8         else:",
            "9             finalList.append(secondHalf[j])",
            "10            j += 1",
            "11    while i < len(firstHalf):",
            "12        finalList.append(firstHalf[i])",
            "13        i += 1",
            "14    while j < len(secondHalf):",
            "15        finalList.append(secondHalf[j])",
            "16        j += 1",
            "17    return finalList"]
errorsor5=[ "1  def merge(firstHalf, secondHalf):",
            "2     finalList = []",
            "3     i, j = 0",
            "4     while i < len(firstHalf) and j < len(secondHalf):",
            "5         if firstHalf[i] >= secondHalf[j]:",
            "6             finalList.append(firstHalf[i])",
            "7             i += 1",
            "8         else:",
            "9             finalList.append(secondHalf[j])",
            "10            j += 1",
            "11    while i < len(firstHalf):",
            "12       finalList.append(firstHalf[i])",
            "13       i += 1",
            "14    while j < len(secondHalf):",
            "15        finalList.append(secondHalf[j])",
            "16        j += 1",
            "17    return finalList",
            "18 def sort(list):",
            "19    length = len(list)",
            "20    if length < 2:",
            "21        return list",
            "22    else:",
            "23        firstHalf = list[:length//2]",
            "24        secondHalf = list[length//2:]",
            "25    return merge(sort(firstHalf), sort(secondHalf))" ]
errorsor6=[ "18 def sort(list):",
            "19    length = len(list)",
            "20    if length < 2:",
            "21        return list",
            "22    else:",
            "23        firstHalf = list[:length//2]",
            "24        secondHalf = list[length//2:]",
            "25    return merge(firstHalf, secondHalf)" ]

error1 = Question("Merge Sort worst case TIME complexity", mergeSort, ["O(logn)", "O(nlogn)", "O(n)", "O(n^2)"], 1)
error2 = Question("Merge Sort SPACE complexity", mergeSort, ["O(logn)", "O(nlogn)", "O(n)", "O(n^2)"], 2)
error3 = Question("Identify the error:", errorsor3, ["Line 1", "Line 4", "Line 5", "Line 2"], 3)
error4 = Question("Change one line to make this ascending:", mergeSort, ["Line 11", "Line 5", "Line 25", "Line 4"], 1)
error5 = Question("Change one line to make this descending:", errorsor5, ["Line 11", "Line 5", "Line 25", "Line 4"], 1)
error6 = Question("Identify the error:", errorsor6, ["Line 20", "Line 24", "Line 25", "Line 23"], 2)
error7 = Question("How does merge sort work:", mergeSort, ["Split main array once then sort left and right side. Merge both sides together and put lower value first.",
                                                           "split subarrays until subarrays are one element: merge subarrays together and put the lowest value first.",
                                                           "Generate two pivot element at the first element and order the rest of the array around it.",
                                                           "Create two arrays and merge them together"], 1)

errors = [error1, error2, error3, error4, error5, error6, error7]