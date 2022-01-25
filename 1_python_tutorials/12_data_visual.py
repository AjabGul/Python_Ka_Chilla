# Steps in data visualization

# step 1: import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# step 2: set a theme
sns.set_theme(style="ticks", color_codes=True)

# step 3: import data set
titanic = sns.load_dataset("titanic")
print(titanic)

# # step 4 basic countplot with one veriable
# p = sns.countplot(x="sex", data=titanic)
# plt.show()

# step 5 basic plot graph with 2 variables using hue
p = sns.countplot(x="sex", data=titanic, hue="class")
plt.show()
