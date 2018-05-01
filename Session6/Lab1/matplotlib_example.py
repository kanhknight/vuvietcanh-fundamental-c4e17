import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

# 1. Prepare data
loai_may = [18, 4, 2]
# 2. Prepare labels
ten_may = ["PC", "Mac", "Linux"]

# 3. Draw pie
pyplot.title("PC vs Mac vs Linux usage")
pyplot.pie(loai_may, labels=ten_may, autopct="%.1f%%", shadow=True, explode=[0,0.1,0.1])
pyplot.axis("equal")

# 4.Show
pyplot.show()