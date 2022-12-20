def hello():
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield 3


res = hello()  # 返回一个生成器
print(next(res))