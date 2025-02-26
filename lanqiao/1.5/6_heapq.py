# # heapq
# # 堆：完全二叉树，每个节点小于等于子节点(默认为最小堆) --> 父小于两个子
# # 每个节点k都有两个子节点2k+1与2k+2
# import heapq


# # heapify(a) 会原地将列表 a 重新排列，使其满足最小堆的性质
# a = [5, 3, 8, 1, 2]
# heapq.heapify(a)  # 将 a 转换为最小堆
# print(a)
# # 可能的输出：[1, 2, 8, 3, 5] 不唯一，但堆顶是最小的


# # heappop(a) 删除并返回 最小元素，同时保证剩余元素仍然是最小堆 
# a = [5, 3, 8, 1, 2]
# heapq.heapify(a)
# heapq.heappop(a)  
# print(a)
# # 也可以这样一步步输出最小元素  可以加个负号实现大根堆


# # heappush(a, x) 会将元素 x 插入到 a，并保持 a 仍然是最小堆
# a = [5,3,4,6,1]
# heapq.heapify(a)  # 先转换成最小堆
# heapq.heappush(a, 0)  # 插入元素 0
# print(a)


# # heapreplace(a, x) 先弹出最小元素，然后插入 x，比 heappop() + heappush() 更高效
# a = [5,3,4,6,1]
# heapq.heapify(a)  
# heapq.heapreplace(a, 2)  
# print(a)

# # 普通列表

# # 适用于一次性排序，但频繁插入/删除不高效。
# # min(list) → O(n)，sorted(list) → O(n log n)。


# # 堆（heapq）

# # 适用于动态数据流，如优先队列、获取最小值、维护前 K 个最小值。
# # heappop() → O(log n)，heappush() → O(log n)。
# # 如果你经常需要获取最小元素，或者管理大量动态数据， 堆是更好的选择！