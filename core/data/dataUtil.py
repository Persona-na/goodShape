import datetime

from core.models.food import Food


# 添加新食物
def add_food(food):
    with open(file='food.csv',mode='a',encoding='utf-8') as f:
        f.write(food.to_str())
    f.close()

# 添加进食记录
def add_intake(food,n):
    date=datetime.datetime.now().date()
    with open(file='intake.csv',mode='a',encoding='utf-8') as f:
        f.write()



if __name__ == '__main__':
    # food=Food('鸡腿','0','20','10')
    # add_food(food)
    add_intake(123,1)