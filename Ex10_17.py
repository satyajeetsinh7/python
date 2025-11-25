# a. Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
import matplotlib.pyplot as plt

x_axis = [1, 2, 3, 4, 5]
y_axis = [2, 3, 5, 7, 11]

plt.plot(x_axis, y_axis)

plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Sample Line Plot')

plt.show()

# b. Write a Python program to plot two or more lines on same plot with suitable legends of each line.
import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y1 = [20, 40, 10, 30]
y2 = [40, 10, 30, 20]

plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Two Lines on One Plot')

plt.legend()
plt.show()

# c. Write a Python programming to display a bar chart of the popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(languages, popularity)

plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")

plt.show()