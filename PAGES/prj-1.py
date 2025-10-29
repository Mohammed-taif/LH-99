import matplotlib.pyplot as plt
import statistics
import os
import webbrowser

subjects = ['Maths', 'Science', 'English']
marks = {
    'A': [90, 86, 70],
    'B': [64, 30, 50],
    'C': [60, 80, 90]
}

print(marks)
print('\n')
print("AVERAGE MARKS OF EACH SUBJECTS :\n")

# THIS BLOCK OF CODE FINDS THE AVERAGE MARKS OF EACH SUBJECT
for i, subject in enumerate(subjects):
    subject_marks = [marks[student][i] for student in marks]
    avg = statistics.mean(subject_marks)
    print(f"{subject}: {avg:.2f}")
print("\n")

# THIS BLOCK OF CODE FINDS THE SUBJECT WITH HIGHEST AND LOWEST AVERAGE
top_avg = 0
top_subject = None
for i, subject in enumerate(subjects):
    subject_marks = [marks[student][i] for student in marks]
    avg = statistics.mean(subject_marks)
    if avg > top_avg:
        top_avg = avg
        top_subject = subject
print("SUBJECT WITH HIGHEST AVERAGE :")
print(f"{top_subject} :", top_avg)

print("\n")
low_avg = 100
low_subject = None
for i, subject in enumerate(subjects):
    subject_marks = [marks[student][i] for student in marks]
    avg = statistics.mean(subject_marks)
    if avg < low_avg:
        low_avg = avg
        low_subject = subject
print("SUBJECT WITH LOWEST AVERAGE :")
print(f"{low_subject} :", low_avg)
print("\n")

# THIS BLOCK OF CODE FINDS THE AVERAGE, MEDIAN, MODE AND STANDARD DEVIATION
def st_mean(std):
    print(f"MARKS ANALYSIS REPORT OF {std}")
    print("Average :", statistics.mean(marks[std]))
    print("Median :", statistics.median(marks[std]))
    print("Mode :", statistics.mode(marks[std]))
    print("Standard Deviation :", statistics.stdev(marks[std]))
    print('\n')


# THIS BLOCK OF CODE PRINTS THE STUDENT PERFORMANCE ANALYSIS REPORT
print("STUDENT PERFORMANCE ANALYSIS REPORT :\n")
for students in marks:
    st_mean(students)

# THIS BLOCK OF CODE FINDS THE TOP PERFORMER
top_avg = 0
top_std = None
for students in marks:
    avg = statistics.mean(marks[students])
    if avg > top_avg:
        top_avg = avg
        top_std = students
print(f"TOP PERFORMER :{top_std}\nAVERAGE :{top_avg}")

# THIS BLOCK OF CODE FINDS THE WEAK PERFORMER
low_avg = 100
low_std = None
for students in marks:
    avg = statistics.mean(marks[students])
    if avg < low_avg:
        low_avg = avg
        low_std = students
print(f"WEAK PERFORMER :{low_std}\nAVERAGE :{low_avg}")

# Calculate average marks for each subject
subject_avgs = []
for i, subject in enumerate(subjects):
    subject_marks = [marks[student][i] for student in marks]
    avg = statistics.mean(subject_marks)
    subject_avgs.append(avg)

# Prepare data for graphs
student_names = list(marks.keys())
student_avgs = [statistics.mean(marks[student]) for student in marks]

# Save graphs instead of showing
plt.bar(subjects, subject_avgs, color="skyblue")
plt.title("Average Marks per Subject")
plt.ylabel("Average Marks")
plt.savefig("subject_avg.png")
plt.close()

plt.bar(student_names, student_avgs, color="orange")
plt.title("Average Marks per Student")
plt.ylabel("Average Marks")
plt.savefig("student_avg.png")
plt.close()

# Final HTML
html_content = f"""
<html>
<head>
  <style>
    body {{
      margin: 0;
      height: 100vh;
      justify-content: center;
      align-items: center;
      color: white;
      font-family: Arial, sans-serif;
      background: linear-gradient(-45deg, #ff6ec4, #7873f5, #17ead9, #fce38a);
      background-size: 400% 400%;
      animation: gradient 10s ease infinite;
    }}
    @keyframes gradient {{
      0% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
      100% {{ background-position: 0% 50%; }}
    }}
  </style>
</head>
<body bgcolor="lightyellow" text="black">

    <h1 align="center" style="color: darkblue;">Student Performance Report</h1>

    <h2 style="color: darkgreen;">Marks Table</h2>
    <table border="1" cellpadding="5" cellspacing="0" width="70%" align="center" bgcolor="lightcyan">
        <tr bgcolor="red">
            <th>Student</th>
            <th>Maths</th>
            <th>Science</th>
            <th>English</th>
        </tr>
        <tr bgcolor="blue">
            <td>A</td>
            <td>90</td>
            <td>86</td>
            <td>70</td>
        </tr>
        <tr bgcolor="blue">
            <td>B</td>
            <td>64</td>
            <td>30</td>
            <td>50</td>
        </tr>
        <tr bgcolor="blue">
            <td>C</td>
            <td>60</td>
            <td>80</td>
            <td>90</td>
        </tr>
    </table>

    <h2 style="color: darkgreen;">Overall Analysis</h2>
    <ul>
        <li><b>Top Performer:</b> {top_std} ({top_avg:.2f})</li>
        <li><b>Weak Performer:</b> {low_std} ({low_avg:.2f})</li>
        <li><b>Strongest Subject:</b> {top_subject} ({max(subject_avgs):.2f})</li>
        <li><b>Weakest Subject:</b> {low_subject} ({min(subject_avgs):.2f})</li>
    </ul>

    <h2 style="color: darkgreen;">Graphs</h2>
    <div align="center">
        <img src="subject_avg.png" width="400"><br><br>
        <img src="student_avg.png" width="400">
    </div>

    <p align="center" style="color: darkred; font-weight:bold;">
        By: Mohammed Taif, Midhun, Azman
    </p>

</body>
</html>
"""

# Write to HTML file
with open("report.html", "w") as f:
    f.write(html_content)

print("\n✅ Report generated successfully as 'report.html'")
print("📂 Saved in:", os.getcwd())

# Open report automatically
path = os.path.abspath("report.html")
webbrowser.open(f"file://{path}")
