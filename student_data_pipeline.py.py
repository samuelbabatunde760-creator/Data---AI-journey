print("___CLEANED STUDENT DATA ___")
#open the file
with open("student_raw_data.txt", "r") as file:
    for line in file:
        new_line = line.strip()
        part = new_line.split(",")

#If name does not exist
        if not part[0]:
            continue
        name = part[0]
        age = part[1]
        scores_list = part[2:]

#Handle Age      
        try:
            age = int(age)
        except ValueError:
            age = None

#Handle Score
        scores = []
        for s in scores_list:
            if s.isdigit():
                scores.append(int(s))

#Average Score
        if len(scores) > 0:
            average_score = sum(scores)/ len(scores)
        else:
            average_score = 0.0

#Decision Making
        if average_score >= 80:
            status = "Excellent"
        elif 70 <= average_score < 80:
            status = "Good"
        else:
            status = "Need Improvement"

#Final Output
        print(f"{name} ({age}) — Avg: {average_score:.1f} — {status}")