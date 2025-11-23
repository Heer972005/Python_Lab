from plotnine.data import economics
from plotnine import ggplot, aes, geom_line
print(economics)
pl1=(
    ggplot(economics)
    + aes(x="date", y="pop")
    + geom_line()
)
print(pl1)
pl1.save(r"G:\sem-3\python_lab\lab28\plotLab1.png")